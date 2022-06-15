from django.urls import path
from core.survey.views import (
    HomeView, IndexView, UserChoiceCreateView,
    SurveyLisView, questions_view, start_again
    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]