import pprint
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from core.survey.models import Survey, Question, Choice, UserChoice
# Register your models here.

class SessionAdmin(admin.ModelAdmin):
    def user(self, obj):
        session_user = obj.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=session_user)
        return user.email
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    _session_data.allow_tags=True
    list_display=['user', 'session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserChoice)

admin.site.register(Session, SessionAdmin)