# https://www.codewars.com//kata/566be96bb3174e155300001b

def max_ball(v0):
    g = 9.81
    v = (v0 * 1000/3600)
    t = 0
    p = -1

    while True:
        h = v * t * 0.1 - 0.5 * g * t * t * 0.01

        if h > p:
            p = h
        else:
            t -= 1
            break

        t += 1

    return t
