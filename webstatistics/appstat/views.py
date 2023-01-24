from django.shortcuts import render
from django.views import generic
from .models import Question, Choice, Poll


class IndexView(generic.ListView):
    template_name = 'appstat/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.order_by('date_pub')


def questionview(request, poll_id):
    poll_questions = Question.objects.filter(poll_id=poll_id) 
    polling_name = Poll.objects.get(pk=poll_id)
    context = {
        'poll_questions': poll_questions,
        'polling_name': polling_name,
    }
    return render(request, 'appstat/questions.html', context)
   
    
def results(request, poll_id):
    poll_questions = Question.objects.filter(poll_id=poll_id)
    polling_name = Poll.objects.get(pk=poll_id)
    try: 
        for question in poll_questions:
            selected_choice = question.choices.get(pk=request.POST[question.question_text]) 
            selected_choice.votes +=1
            selected_choice.save()
    except(Choice.DoesNotExist, KeyError):
        context = {
            'poll_questions': poll_questions,
            'polling_name' : polling_name,
            'error_message':'Проголосуйте во всех вопросах!',
        }
        return render(request, 'appstat/questions.html', context)
    else:       
        context = {
            'poll_questions' : poll_questions,
            'polling_name': polling_name,    
        }
        return render(request, 'appstat/results.html', context)