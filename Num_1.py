# https://www.codewars.com//kata/5b077ebdaf15be5c7f000077

def count_sheep(n):
    k = ""
    if n > 0:
        for i in range(1, n + 1):
            k = k + str(i) + " sheep..."
    else:
        k = ""
    return k