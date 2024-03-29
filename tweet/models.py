from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tweet(models.Model):
    hashtag_choices = [
        ('Tarix', '#Tarix'),
        ('Sport', '#Sport'),
        ('Phone', '#Phone'),
        ('Siyosat', '#Siyosat'),
        ('Madaniy', '#Madaniy'),
        ('Kitob', '#Kitob'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hashtag = models.CharField(max_length=20, choices=hashtag_choices, default='tarix')
    question = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    parent_tweet = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_like')
    comment_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.question}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text}"