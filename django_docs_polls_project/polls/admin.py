from django.contrib import admin

from .models import Question, Choice, ScaleChoice


class ChoiceInlineAdmin(admin.TabularInline):
    model = Choice


class ScaleChoiceInlineAdmin(admin.TabularInline):
    model = ScaleChoice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInlineAdmin,
        ScaleChoiceInlineAdmin
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(ScaleChoice)