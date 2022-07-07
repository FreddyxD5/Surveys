import json
from django.shortcuts import redirect
from django.http import HttpResponse
from core.survey.models import Survey

def start_again(request):
    request.session.flush()
    messages.success(request, "Hagasmolo de nuevo")
    return redirect('index')



def questions_view(request, slug):        
    print(request)
    interval = request.GET.get('interval','year')    
    print('what?')
    print(interval)
    labels = []
    data = []
    try:
        obj = Survey.objects.get(slug = slug)        
                
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

