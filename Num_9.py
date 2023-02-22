# https://www.codewars.com/kata/57cf50a7eca2603de0000090

def move_ten(st):
    key = 10
    s = ""
    for i in range(len(st)):
        after = ord(st[i]) + key
        if after > 122:
            after -= 26
        s += chr(after)

    return s