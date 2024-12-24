import os
import logging
from django.core.management.base import BaseCommand
from game.models import Word

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Import a dictionary into database'


    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to file to import')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path) as f:
            lines = f.readlines()
            for line in lines:
                save_word_to_database(line)
            

def save_word_to_database(word: str) -> None:
    try:
        Word(word=word).save()
    except Exception:
        logger.warning(f"Couldn't import word: {word}")





