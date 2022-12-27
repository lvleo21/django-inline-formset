from django.contrib import admin
from core.models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=["title", "description"]


@admin.register(Alternative)
class AlternativeAdmin(admin.ModelAdmin):
    list_display=["description", "is_correct", "question"]




