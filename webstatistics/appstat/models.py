import datetime

from django.db import models
from django.utils import timezone


class Poll(models.Model):
    name = models.CharField(max_length=20)
    date_pub = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_pub <= now

    class Meta:
        verbose_name_plural = 'Polls'


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name_plural = 'Questions'


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        
    class Meta:
        verbose_name_plural = 'Choices'
