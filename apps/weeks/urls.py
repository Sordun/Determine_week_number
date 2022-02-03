from django.urls import path

from . import views


urlpatterns = [
    path("", views.week_number, name="week_number"),
    path("answer_weeks/", views.answer_weeks, name="answer_weeks"),
]
