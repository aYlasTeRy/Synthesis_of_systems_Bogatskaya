# https://www.codewars.com/kata/54b724efac3d5402db00065e

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    s = ''
    morse_code = morse_code.strip()
    morse_code = morse_code.replace('   ' ,' $')

    morse = morse_code.split(" ")
    for i in range(len(morse)):

        if morse[i][0] == "$":
            s += " "
            s += MORSE_CODE[morse[i][1:]]

        else:
            s += MORSE_CODE[morse[i]]

    return s