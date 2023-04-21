# https://leetcode.com/problems/search-a-2d-matrix/submissions/937384498/
"""
Вам будет предоставлена m x n целочисленная матрица matrix со следующими двумя свойствами:
Каждая строка отсортирована в порядке неубывания.
Первое целое число каждой строки больше последнего целого числа предыдущей строки.
Учитывая целое число target, верните, true если target находится в matrix или false.
"""


def Binsearch_matrix(matrix, target, left_m, right_m):
    if left_m > right_m:
        return False
    mid_m = (left_m + right_m) // 2
    if matrix[mid_m][-1] < target:
        return Binsearch_matrix(matrix, target, mid_m + 1, right_m)
    elif matrix[mid_m][0] > target:
        return Binsearch_matrix(matrix, target, left_m, mid_m - 1)
    else:
        return Binsearch(matrix, target, mid_m, 0, len(matrix[0]) - 1)


def Binsearch(matrix, target, mid_m, left, right):
    mid = (left + right) // 2
    if matrix[mid_m][mid] != target and left >= right:
        return False

    if matrix[mid_m][mid] == target:
        return True
    elif matrix[mid_m][mid] > target:
        return Binsearch(matrix, target, mid_m, left, mid - 1)
    else:
        return Binsearch(matrix, target, mid_m, mid + 1, right)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return Binsearch_matrix(matrix, target, 0, len(matrix) - 1)