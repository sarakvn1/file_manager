from django.contrib import admin
from django.urls import path
from main.views import LogInView,SignUpView,ConverterView

urlpatterns = [
    path('login', LogInView.as_view()),
    path('signup', SignUpView.as_view()),
    path('convert', ConverterView.as_view()),

]
