from django.shortcuts import render

from .forms import QueryForm
from .models import *
import requests, json

def _unique_users(res):
    users = []
    for result in res:
        users.append((result["user"]["handle"], result["user"]["name"]))
        if "mentions" in result:
            for mention in result["mentions"]:
                users.append((mention["handle"], mention["name"]))

    return list(set(users))

def index(request):
    context = {}
    if request.GET.get("query"):
        form = QueryForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            context["form"] = form

            try:
                saved_query = Queries.objects.get(query = query)
                print(saved_query)
                try:
                    results = Results.objects.get(query = saved_query)
                    print(results)
                except Results.DoesNotExist:
                    print("NO RESULT")
            except Queries.DoesNotExist:
                print("saving...")
                result = requests.get(f"https://social.jkaref.com/social_media_service/search-api?query={query}")
                results = json.loads(result.text)
                query_save = Queries(query = query, result_count = results["res_count"])
                query_save.save()
                res = results["res"]
                users = _unique_users(res)
                for user in users:
                    handle, name = user
                    try:
                        Users.objects.get(handle = handle)
                    except Users.DoesNotExist:
                        Users(handle = handle, name = name).save()
                for result in res:
                    result_save = Results(
                            full_text = result["full_text"],
                            date = result["when"],
                            query = query_save,
                            author = Users.objects.get(handle = result["user"]["handle"])
                            )

                    if "hashtag" in result:
                        for hashtag in result["hashtags"]:
                            hstg = Hashtags(text=hashtag["text"]).save()
                            result_save.hashtag.add(hstg)

                    if "mentions" in result:
                        for mention in result["mentions"]:
                            result_save.mention.add(Users.objects.get(handle = mention["handle"]))

                    result_save.save()

                context["result"] = results["res"][0]

    else:
        context["form"] = QueryForm()
    return render(request, "query/index.html", context)
