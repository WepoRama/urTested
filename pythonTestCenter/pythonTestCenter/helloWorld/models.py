from django.db import models

# Create your models here.
class Test(models.Model):
    test_id = models.IntegerField(primary_key=true)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    expires_date = models.DateField()

class Question(models.Model):
    question_id = models.IntegerField(primary_key=true)
    test_id = models.IntegerField()
    question = models.CharField(max_length=50)
    points = models.IntegerField()
class Answer (models.Model):
    answer_id = models.IntegerField(primary_key=true)
    question_id = models.IntegerField()
    correct = models.BooleanField()
    answer = models.CharField(max_length=50)
