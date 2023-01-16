from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Poll


#def index(request):
#    latest_question_list = Question.objects.order_by('-question_text')[:5]
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return render(request, 'appstat/index.html', context)

# def poll(request, poll_id):
#    return HttpResponse(f"You're looking at poll {poll_id}")
class IndexView(generic.ListView):
    template_name = 'appstat/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.order_by('date_pub')


#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'appstat/questions.html', {'question': question})
#class QuestionView(generic.ListView):
#    model = Question
#    template_name = 'appstat/questions.html'
#    context_object_name = 'poll_questions'
#
#    def get_queryset(self):
#        return Question.objects.filter(Question, pk='question_id')
def questionview(request, poll_id):
    poll_questions = Question.objects.filter(poll_id=poll_id) 
    polling_name = Poll.objects.get(pk=poll_id)
    context = {
        'poll_questions': poll_questions,
        'polling_name': polling_name,
    }
    return render(request, 'appstat/questions.html', context)
   
    
def results(request, poll_id):
    question = get_object_or_404(Question, pk=poll_id)
    polling_name = Poll.objects.get(pk=poll_id)
    context = {
        'question': question,
        'polling_name': polling_name,
    }
    return render(request, 'appstat/results.html', context)

    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice']) 
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'appstat/questions.html', {
            'question': question,
            'error_message':'You did not select a choice',
        })
    else: 
        selected_choice.votes +=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polling:results'), args=(question.id,))


