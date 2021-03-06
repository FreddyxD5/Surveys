
import datetime
import redis
from django.conf import settings

from core.survey.models import Question


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