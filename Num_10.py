# https://www.codewars.com//kata/573d498eb90ccf20a000002a

def decode(strng):
    line = ''
    for i in strng:
        if i == '5':
            element = '0'
        elif i == '0':
            element = '5'
        else:
            between = 10 - int(i)
            element = str(between)

        line += element

    return (line)