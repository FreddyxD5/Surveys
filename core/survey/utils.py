
import datetime
import redis
from django.conf import settings

from core.survey.models import Question, Choice


SURVEY_DAYS = 15
survey_end_date = lambda:datetime.date.today() + datetime.timedelta(days=SURVEY_DAYS)

def get_last_survey():
    from core.survey.models import Survey
    survey = Survey.objects.all().order_by('-id')[0]
    return Survey

def get_redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB):
    return redis.Redis(
        host=host,
        port=port,
        db=db
    )




def create_choices(question_id, items, slug):
    query = Question.objects.filter(id=int(question_id)).first()
    for item in items:
        choice_instance = Choice(question=query,choice_text=item, slug=slug)
        choice_instance.save()
    print('-=Opciones para la pregunta creadas correctamente=-')
