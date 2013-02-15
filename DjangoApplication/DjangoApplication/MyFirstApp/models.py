from django.db import models

# See: https://docs.djangoproject.com/en/dev/topics/db/models/
# and: https://docs.djangoproject.com/en/dev/intro/tutorial01/

# Create your models here.
class Test(models.Model):
    test_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    expires_date = models.DateField()

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    test_id = models.ForeignKey(Test)
    question = models.CharField(max_length=50)
    points = models.IntegerField()

class Answer (models.Model):
    answer_id = models.IntegerField(primary_key=True)
    question_id = models.ForeignKey(Question)
    correct = models.BooleanField()
    answer = models.CharField(max_length=50)
