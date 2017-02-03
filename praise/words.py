import random

from .adjective import adjective
from .adverb import adverb
from .exclamation import exclamation
from .smiley import smiley
from .verb import created, creating


def get_one_word_dict():
    return {
        'adjective': random.choice(adjective),
        'adverb': random.choice(adverb),
        'exclamation': random.choice(exclamation),
        'smiley': random.choice(smiley),
        'created': random.choice(created),
        'creating': random.choice(creating)
    }
