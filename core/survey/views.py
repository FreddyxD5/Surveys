from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def detail(request, question_id):
    return HttpResponse(f"You're looking for a question {question_id}")

def results(request, question_id):
    response = f"You're looking at the results of questions {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting  on question {question_id}")