# https://www.codewars.com/kata/5592fc599a7f40adac0000a8

def sum_diagonals(matrix):
    suma = 0
    j = -1
    if matrix == [[]]:
        return 0

    else:
        for i in range(len(matrix)):
            suma += matrix[i][i]
            suma += matrix[i][j]
            j -= 1
    return suma