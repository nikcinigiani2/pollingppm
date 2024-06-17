from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='polls')
    responded_users = models.ManyToManyField(User, related_name='answered_polls', blank=True)


    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200, default='default_value')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text






