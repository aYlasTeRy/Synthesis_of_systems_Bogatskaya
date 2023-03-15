# https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(sequence):
    l1 = 0
    l = []
    if len(sequence) == 0:
        return []

    l.append(sequence[0])

    for l2 in range(len(sequence)):
        if sequence[l1] != sequence[l2]:
            l1 = l2
            l.append(sequence[l1])

    return l


