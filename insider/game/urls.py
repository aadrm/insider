from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show-word/', views.show_word, name='show_word'),
    path('hide-word/', views.hide_word, name='hide_word'),
    path('next-word/', views.next_word, name='next_word'),
    path('reset-words/', views.reset_words, name='reset_words'),
]
