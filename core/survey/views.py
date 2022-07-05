import json
import logging

from celery.utils.log import get_task_logger

from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from core.survey.models import UserChoice, Question, Survey
from core.survey.tasks import increment_vote, increment_counter


from core.survey.mixins import RandomQuestionMixin
# Create your views here.

logger = get_task_logger(__name__)




class HomeView(RandomQuestionMixin, TemplateView):
    template_name = 'home.html'


class IndexView(RandomQuestionMixin, TemplateView):
    template_name = 'survey/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        question = self.get_random_question()
        if question is not None:
            context.update({'questions':[question]})
        context['current_progress'] = self.get_current_progress()        
        return context



class UserChoiceCreateView(RandomQuestionMixin, CreateView):
    model = UserChoice
    fields = ['question','choice']

    def get_success_url(self):
        return reverse('index')

    def form_invalid(self, form):
        responsedict = {
            'form':form.errors,
            'status':False
        }
        return HttpResponse(json.dumps(responsedict))

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        else:
            form.instance.session_key = self.current_session_key
        
        form.save()
        increment_vote.delay(form.instance.choice_id)
        increment_counter.delay(form.instance.choice_id)
        messages.success(self.request, 'Your choice was save successfully.')
        return super().form_valid(form)


class SurveyLisView(LoginRequiredMixin, ListView):
    model = Survey


class SurveyDetail(LoginRequiredMixin, DetailView):
    model = Survey