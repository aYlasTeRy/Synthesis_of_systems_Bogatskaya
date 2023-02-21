# https://www.codewars.com//kata/5ab6538b379d20ad880000ab

def area_or_perimeter(l , w):
    if l == w:
        s = l ** 2
    else:
        s = 2 * l + 2 * w
    return s


