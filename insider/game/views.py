import logging
from django.http import HttpResponse
from django.shortcuts import render
from .game_utils import (
    get_next_word,
    get_current_word_or_start,
)

logger = logging.getLogger('django')

def home(request):
    return render(request, 'home.html')

def show_word(request):
    word = get_current_word_or_start(request)
    context = {
        'word': word
    }
    return render(request, 'show_word.html', context)

def next_word(request):
    get_next_word(request)

    return hide_word(request)
    
def reset_words(request):
    if 'played_words' in request.session and request.session['played_words']:
        request.session['played_words'] = []
        return HttpResponse(status=200)
    return HttpResponse(status=202)


def hide_word(request):
    return render(request, 'hide_word.html')
    

