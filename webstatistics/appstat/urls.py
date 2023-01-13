from django.urls import path

from . import views

app_name = 'polling'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:poll_id>/', views.poll, name='poll'),
    path('<int:poll_id>/', views.questionview, name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]