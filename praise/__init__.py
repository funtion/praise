import string
from .words import Words


def praise(template="You are ${adjective}!"):
    if template == None:
        template = "None"
    template = string.Template(template)
    result = template.substitute(Words())
    return result
