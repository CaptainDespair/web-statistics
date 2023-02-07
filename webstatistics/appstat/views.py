from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Question, Choice, Poll


class IndexView(generic.ListView):
    template_name = 'appstat/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last ten published polls (not including future)."""
        return Poll.objects.filter(date_pub__lte=timezone.now()).order_by('date_pub')[:10]


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
        selected_choice_list = []
        max_questions = []
        for question in poll_questions:
               
            selected_choice = question.choices.get(pk=request.POST[question.question_text]) 
            selected_choice.votes +=1
            selected_choice.save()
            selected_choice_list.append(selected_choice.votes)
            max_choice = max(selected_choice_list)
            print(max_choice)
            selected_choice_list = []
            max_questions.append(max_choice)      
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
            'max_questions': max_questions,    
        }
        return render(request, 'appstat/results.html', context)