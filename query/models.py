from django.db import models

class Queries(models.Model):
    query = models.CharField(max_length=200)
    result_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Query: {self.query} ({self.result_count} results)"


class Users(models.Model):
    handle = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)

class Hashtags(models.Model):
    text = models.CharField(max_length=200, unique=True)

class Results(models.Model):
    full_text = models.CharField(max_length=200)
    date = models.DateTimeField()
    query = models.ForeignKey(Queries, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, related_name="author", on_delete=models.CASCADE)
    hashtag = models.ManyToManyField(Hashtags)
    mention = models.ManyToManyField(Users)


    def __str__(self):
        out = self.author.name + "\n\n"
        out += "@" + self.author.handle + "\n\n"
        out += self.full_text + "\n"
        if self.mention.all():
            out += "\n"
            for mention in self.mention.all():
                out += "@" + mention.user.handle + "\n"
        if self.hashtag.all():
            out += "\n"
            for hashtag in self.hashtag.all():
                out += "#" + hashtag.text + "\n"
        return out
