from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    expires_date = models.DateField()

class Question(models.Model):
    test = models.ForeignKey(Test)
    question = models.CharField(max_length=512)
    points = models.IntegerField()

class Answer(models.Model):
    question = models.ForeignKey(Question)
    correct = models.BooleanField()
    answer = models.CharField(max_length=256)

class Score(models.Model):
    test = models.ForeignKey(Test)
    score = models.IntegerField()
    name = models.CharField(max_length=50)

## class for user and userrole
#class User (models.Model):
#    username = models.CharField(max_length=30)
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    email = models.CharField(max_length=30)
#    password = models.CharField(max_length=30)
#    is_staff = models.BooleanField()
#    is_superuser = models.BooleanField()
#    last_login = models.DateTimeField()
