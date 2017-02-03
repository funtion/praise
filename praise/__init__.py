import string
from .words import get_one_word_dict


def praise(template="You are ${adjective}!"):
    if template == None:
        template = "None"
    template = string.Template(template)
    words = get_one_word_dict()
    result = template.substitute(words)
    return result
