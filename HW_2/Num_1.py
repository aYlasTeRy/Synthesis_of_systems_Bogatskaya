# https://www.codewars.com//kata/5a262cfb8f27f217f700000b

def solve(a,b):
    st = ''
    for i in a:
        if b.find(i) == -1:
            st = st + i
    for j in b:
        if a.find(j) == -1:
            st = st + j

    return st