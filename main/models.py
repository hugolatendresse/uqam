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

    def __str__(self):
        return self.atext
