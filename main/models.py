from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    qtext = models.CharField(max_length=1024)
    qnumber = models.IntegerField()
    # qanswers = (('A1', 'this is answer1'), ('A2', 'Ceci est reponse 2'))

    def __str__(self):
        return self.qtext


class Answer(models.Model):
    atext = models.CharField(max_length=1024)
    qnumber = models.IntegerField()
    anumber = models.IntegerField()

    def __str__(self):
        return self.atext

class RandomUser(models.Model):
    q1 = models.CharField(max_length=1024, editable=False, default="Ask")
    q2 = models.CharField(max_length=1024, editable=False, default="Ask")
    q3 = models.CharField(max_length=1024, editable=False, default="Ask")
    q4 = models.CharField(max_length=1024, editable=False, default="Ask")
    q5 = models.CharField(max_length=1024, editable=False, default="Ask")
    q6 = models.CharField(max_length=1024, editable=False, default="Ask")
