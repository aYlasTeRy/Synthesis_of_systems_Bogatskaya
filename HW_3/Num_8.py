# https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    l = 0
    if len(text) == 0:
        return ''
    text_end = text[0]
    for r in range(1, len(text)):
        if text[r] == '-' or text[r] == '_':
            l = r + 1
            text_end += text[r + 1].title()
        elif r != l:
            text_end += text[r]

    return text_end