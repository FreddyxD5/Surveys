import pprint
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from import_export import resources
from import_export.admin import ImportExportModelAdmin



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

class SurveyResource(resources.ModelResource):
    class Meta:
        model = Survey


class SurveyAdmin(ImportExportModelAdmin):
    resource_class = SurveyResource


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question


class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource


class ChoiceResource(resources.ModelResource):
    class Meta:
        model = Choice

class ChoiceAdmin(ImportExportModelAdmin):
    resource_class = ChoiceResource

class UserChoiceResource(resources.ModelResource):
    class Meta:
        model = UserChoice

class UserChoiceAdmin(ImportExportModelAdmin):
    resource_class = UserChoiceResource


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(UserChoice, UserChoiceAdmin)

admin.site.register(Session, SessionAdmin)