import random

from .models import Word


def get_next_word(played_words: list[str] = None) -> str:
    words = Word.objects.all()
    unplayed_words = words.exclude(word__in=played_words)
    
    return random.choice(unplayed_words).word
