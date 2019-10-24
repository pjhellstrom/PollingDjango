from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header = 'DjangoPoll Admin'
admin.site.site_title = 'DjangoPoll Admin'
admin.site.index_title = 'Hi, this is the DjangoPoll Admin page'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': [
                  'published_date'], 'classes': ['collapse']}),
                 ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
