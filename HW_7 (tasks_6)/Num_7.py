# https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
Массив arr является горой. Верните вершину
"""

def Binsearch(arr, left, right):
    mid = (left + right) // 2
    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return mid
    elif arr[mid] > arr[mid - 1]:
        return Binsearch(arr, mid + 1, right)
    else:
        return Binsearch(arr, left, mid - 1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return Binsearch(arr, 0, len(arr))