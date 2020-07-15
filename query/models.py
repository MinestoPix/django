from django.db import models

class Queries(models.Model):
    query = models.CharField(max_length=200)
    result_count = models.IntegerField(default=0)


class Users(models.Model):
    handle = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)

class Hashtags(models.Model):
    text = models.CharField(max_length=200, unique=True)

class Results(models.Model):
    full_text = models.CharField(max_length=200)
    date = models.DateTimeField()
    query = models.ForeignKey(Queries, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    hashtag = models.ManyToManyField(Hashtags)


    def __str__(self):
        print(self.author.name)
        print("@" + self.author.handle)
        print()
        print(self.full_text)
        if self.mention_set.all():
            print()
            for mention in self.mention_set.all():
                print("@" + mention.user.handle)
        if self.hashtag_set.all():
            print()
            for hashtag in self.hashtag_set.all():
                print("#" + hashtag.text)

class Mentions(models.Model):
    result = models.ForeignKey(Results, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
