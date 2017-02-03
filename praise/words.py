import random

from .adjective import adjective
from .adverb import adverb
from .exclamation import exclamation
from .smiley import smiley
from .verb import created, creating


class Words(dict):

    def __getitem__(self, key):
        word_dict = {
            'adjective': random.choice(adjective),
            'adverb': random.choice(adverb),
            'exclamation': random.choice(exclamation),
            'smiley': random.choice(smiley),
            'created': random.choice(created),
            'creating': random.choice(creating)
        }
        if key.lower() in word_dict.keys():
            result = word_dict[key.lower()]
        else:
            result = "${%s}" % key

        if key.isupper():
            result = result.upper()
        elif key[0].isupper() and key[1:].islower():
            result = result[0].upper() + result[1:]
        return result
