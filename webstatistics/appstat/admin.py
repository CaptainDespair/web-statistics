from django.contrib import admin
from .models import Poll, Question, Choice


class QuestionsOnePage(admin.StackedInline):
    model = Question 
    extra = 3


class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_pub', 'was_published_recently')
    list_filter = ['date_pub']
    search_fields = ['name']
    fieldsets = [
        ('Date information', {'fields': ['date_pub'], 'classes':['collapse']}),
        (None,               {'fields': ['name']}),
        ]
    inlines = [QuestionsOnePage]


class ChoicesOnePage(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'poll')
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Опрос', {'fields': ['poll']}),
    ]
    inlines = [ChoicesOnePage]


admin.site.register(Choice) 
admin.site.register(Question, QuestionAdmin)
admin.site.register(Poll, PollAdmin)

