import random
import logging
from django.http import HttpResponse
from django.shortcuts import render
from .game_utils import get_next_word

logger = logging.getLogger(__name__)
# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_word(request):
    word = request.session['word'] if 'word' in request.session else get_next_word(request.session['played_words'])
    context = {
        'word': word
    }
    return render(request, 'show_word.html', context)

def next_word(request):

    if 'played_words' not in request.session:
        request.session['played_words'] = []
    request.session['played_words'].append(request.session['word'])
    request.session['word'] = get_next_word(request.session['played_words'])
    print(request.session['played_words'])
    return hide_word(request)
    
def reset_words(request):
    if 'played_words' in request.session and request.session['played_words']:
        request.session['played_words'] = []
        return HttpResponse(status=200)
    return HttpResponse(status=202)


def hide_word(request):
    return render(request, 'hide_word.html')
    
