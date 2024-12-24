import logging
import random

from .models import Word

logger = logging.getLogger('django')

def update_played_words(request, word):
    if 'played_words' not in request.session:
        logger.info("played_words not in session, initializing")
        request.session['played_words'] = []
    request.session['played_words'].append(word)
    logger.info(f"Played words: {request.session['played_words']}")

def get_played_words(request):
    if 'played_words' not in request.session:
        logger.info("played_words not in session, initializing")
        request.session['played_words'] = []
    return request.session['played_words']


def get_current_word_or_start(request):
    if 'word' not in request.session:
        logger.info("word not in session, initializing")
        request.session['word'] = get_next_word(request)
    return request.session['word']


def get_next_word(request) -> str:
    words = Word.objects.all()
    unplayed_words = words.exclude(word__in=get_played_words(request))
    next_word = random.choice(unplayed_words).word
    update_played_words(request, next_word)
    logger.info(f"Next word: {next_word}")
    request.session['word'] = next_word

