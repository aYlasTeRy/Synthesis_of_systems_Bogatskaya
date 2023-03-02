def maxi(a, *b, low = 1, hi = 100):
    s = max((a,) + b)
    if low < s < hi:
        return s
    elif s <= low:
        return low
    elif s >= hi:
        return hi
