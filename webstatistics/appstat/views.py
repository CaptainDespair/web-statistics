from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, please take a poll for general statistics.')