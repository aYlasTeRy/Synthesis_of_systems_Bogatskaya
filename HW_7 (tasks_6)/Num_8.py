# https://leetcode.com/problems/find-peak-element/
"""
Пиковый элемент - это элемент, который строго больше своих соседей.

Учитывая целочисленный массив с nums0-индексом, найдите пиковый элемент и верните его индекс.
Если массив содержит несколько пиков, верните индекс к любому из пиков.

Вы можете себе это представить nums[-1] = nums[n] = -∞.
Другими словами, элемент всегда считается строго большим, чем соседний элемент, который находится за пределами массива.
"""


def Binsearch(arr, left, right):
    mid = (left + right) // 2
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return 0
        else:
            return 1
    if arr[-1] > arr[-2]:
        return len(arr) - 1

    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return mid
    elif arr[mid] > arr[mid - 1]:
        return Binsearch(arr, mid + 1, right)
    else:
        return Binsearch(arr, left, mid)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return Binsearch(nums, 0, len(nums))
