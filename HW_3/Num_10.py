# https://www.codewars.com/kata/55467aaf72494e3bdc00007f

def is_rotation(s1 ,s2):
    l1 = 0
    l2 = 0
    flag = True

    if l1 == len(s1) and l2 == len(s2):
        return True

    elif len(s1) != len(s2):
        return False

    while l1 < len(s2) - 1:

        if s1[l1] != s2[l2] and flag == True:
            l2 += 1

        elif s1[l1] == s2[l2]:

            flag = False

            if l2 == len(s2) - 1:
                l1 += 1
                l2 = 0
            else:
                l1 += 1
                l2 += 1

        else:
            return False
    return True