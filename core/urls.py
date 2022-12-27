from django.urls import path
from . import views



urlpatterns = [
    path('question/', views.QuestionCreateView.as_view(), name="question_create_view"),
    # path('', ),
]
