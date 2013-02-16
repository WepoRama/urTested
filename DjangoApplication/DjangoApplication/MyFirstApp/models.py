from django.db import models

# See: https://docs.djangoproject.com/en/dev/topics/db/models/
# and: https://docs.djangoproject.com/en/dev/intro/tutorial01/

# Create your models here.
class Test(models.Model):
    #test = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    expires = models.DateField()

class Question(models.Model):
    #question = models.IntegerField(primary_key=True)
    test = models.ForeignKey(Test)
    question = models.CharField(max_length=50)
    points = models.IntegerField()

class Answer (models.Model):
    #answer = models.IntegerField(primary_key=True)
    question = models.ForeignKey(Question)
    correct = models.BooleanField()
    answer = models.CharField(max_length=50)
