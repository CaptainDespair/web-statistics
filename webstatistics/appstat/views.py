from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-question_text')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'appstat/index.html', context)

# def poll(request, poll_id):
#    return HttpResponse(f"You're looking at poll {poll_id}")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'appstat/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(f"Results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Your vote on question is {question_id}")

