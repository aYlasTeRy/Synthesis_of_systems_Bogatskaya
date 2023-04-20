# https://leetcode.com/problems/search-insert-position/
"""
Учитывая отсортированный массив различных целых чисел и целевое значение, верните индекс, если цель найдена.
Если нет, верните индекс, где он был бы, если бы он был вставлен по порядку.
"""


def Binsearch(nums, target, left, right):
    mid = left + (right - left) // 2
    if left > right:
        return left
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return Binsearch(nums, target, left, mid - 1)
    else:
        return Binsearch(nums, target, mid + 1, right)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return Binsearch(nums, target, 0, len(nums) - 1)
