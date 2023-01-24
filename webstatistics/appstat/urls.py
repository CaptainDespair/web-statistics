from django.urls import path

from . import views

app_name = 'polling'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:poll_id>/', views.questionview, name='questions'),
    path('<int:poll_id>/results/', views.results, name='results'), 
]