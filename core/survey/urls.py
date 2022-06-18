from django.urls import path
from core.survey.views import (
    HomeView, IndexView, UserChoiceCreateView,
    SurveyLisView, SurveyDetail
    )

from core.survey.views_functions import questions_view, start_again

urlpatterns = [
    path('', HomeView.as_view(), name='home'),    
    path('index',IndexView.as_view(), name='index'),
    path('start-again', start_again, name='start_again'),
    path('question_view/<int:question_id>/choice', UserChoiceCreateView.as_view(), name='user_choice'),
    path('surveys/', SurveyLisView.as_view(), name='survey_list'),
    path('surveys/detail/<slug:slug>', SurveyDetail.as_view(), name='survey_detail'),
    path('surveys/<slug:slug>/question.json', questions_view, name='questions_view'),

]