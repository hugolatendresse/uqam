from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    qtext = models.CharField(max_length=1024)
    qnumber = models.IntegerField()

    def __str__(self):
        return self.qtext


class Answer(models.Model):
    atext = models.CharField(max_length=1024)
    qnumber = models.IntegerField()
    anumber = models.CharField(max_length=1024)
    q_to_ask = models.CharField(max_length=1024, editable=False, default="")

    def __str__(self):
        return self.atext


class Conseil(models.Model):
    ctext = models.CharField(max_length=1024)
    q1 = models.CharField(max_length=1024, editable=False, default="<any>")
    q2 = models.CharField(max_length=1024, editable=False, default="<any>")
    q3 = models.CharField(max_length=1024, editable=False, default="<any>")
    q4 = models.CharField(max_length=1024, editable=False, default="<any>")
    q5 = models.CharField(max_length=1024, editable=False, default="<any>")
    q6 = models.CharField(max_length=1024, editable=False, default="<any>")
    q7 = models.CharField(max_length=1024, editable=False, default="<any>")
    q8 = models.CharField(max_length=1024, editable=False, default="<any>")
    q9 = models.CharField(max_length=1024, editable=False, default="<any>")
    q10 = models.CharField(max_length=1024, editable=False, default="<any>")

    def __str__(self):
        return self.ctext


class RandomUser(models.Model):
    question_cnt = models.IntegerField()
    q1 = models.CharField(max_length=1024, editable=False, default="Ask")
    q2 = models.CharField(max_length=1024, editable=False, default="skip")
    q3 = models.CharField(max_length=1024, editable=False, default="skip")
    q4 = models.CharField(max_length=1024, editable=False, default="skip")
    q5 = models.CharField(max_length=1024, editable=False, default="skip")
    q6 = models.CharField(max_length=1024, editable=False, default="skip")
    q7 = models.CharField(max_length=1024, editable=False, default="skip")
    q8 = models.CharField(max_length=1024, editable=False, default="skip")
    q9 = models.CharField(max_length=1024, editable=False, default="skip")
    q10 = models.CharField(max_length=1024, editable=False, default="skip")

