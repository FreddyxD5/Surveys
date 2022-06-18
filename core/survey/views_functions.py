from django.shortcuts import redirect
from django.http import HttpResponse
from core.survey.models import Survey

def start_again(request):
    request.session.flush()
    messages.success(request, "Hagamolo de nuevo")
    return redirect('index')



def questions_view(request, slug):
    interval = request.GET.get('interval','year')
    labels = []
    data = []
    try:
        obj = Survey.object.get(slug = slug)
        for question in obj.get_top_questions(interval):
            labels.append(question.slug)
            data.append(question.count)

        responsedic = {
            'data':data,
            'labels':labels
        }
    except Survey.DoesNotExist:
        pass

    
    responsedict = {
        'data':data,
        'labels':labels
    }

    return HttpResponse(json.dumps(responsedict))

