# https://www.codewars.com/kata/57a083a57cb1f31db7000028

def powers_of_two(n):
    arr = []
    for item in range(0, n + 1):
        arr.append(2 ** item)
    return arr