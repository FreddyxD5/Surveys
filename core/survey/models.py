import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Survey(models.Model):
    slug = models.SlugField(max_length=20)
    start_date = models.DateField(
        default = datetime.date.today,
        help_text = 'Survey first day'
    )
    end_date = models.DateField(
        default = datetime.date.today,
        help_text = 'Survey last day'
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.slug


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length = 500)
    slug = models.SlugField(max_length=30)
    pub_date = models.DateTimeField()
    is_active= models.BooleanField(default=True)


    def __str__(self):
        return f"{self.slug}: {self.question_text}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)    

    def __str__(self):
        return f"{self.question.slug}: {self.choice_text}"



class UserChoice(models.Model):
    user =models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice =models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add =True, blank=True)
    #Careful with Cookie-Based Sessions.
    #Read using cookie-based session warning
    session_key = models.CharField(max_length=32,null=True)
    


