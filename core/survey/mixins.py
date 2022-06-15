
class RandomQuestionMixin(object):
    @property
    def current_session_key(self):
        if not self.request.session.session_key:
            self.request.session.save()
        session_key = self.request.session.session_key
        return session_key


    def get_random_question(self):
        return Question.objects.random_get(self.current_session_key)
        
    def get_current_progress(self):
        question_count = Question.objects.filter(is_active=True).count()
        user_choices = UserChoice.objects.filter(question__is_active=True)
        user_choices_count = user_choices.filter(**self.session_param()).count()
        return (user_choices_count*100 // question_count) if questions_count  > 0 else 100

    
    def session_param(self):
        if self.request.user.is_authenticated:
            query_params = {'user':self.request.user}
        else:
            query_params = {'session_key':self.current_session_key}
        return query_params
