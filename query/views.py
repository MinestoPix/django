from django.shortcuts import render


def index(request):
    if request.GET.get("query"):
        context = request.GET
    return render(request, "query/index.html", context)

