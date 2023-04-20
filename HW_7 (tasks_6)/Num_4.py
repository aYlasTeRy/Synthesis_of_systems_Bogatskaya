# https://leetcode.com/problems/binary-search/
"""
Учитывая массив целых чисел, nums который отсортирован в порядке возрастания,
и целое число target, напишите функцию для поиска target в nums.
Если target существует, то верните его индекс. В противном случае верните -1.
"""

def Binsearch(nums, target, left, right):
    mid = left + (right - left) // 2
    if nums[mid] != target and left > right:
        return -1
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return Binsearch(nums, target, left, mid - 1)
    else:
        return Binsearch(nums, target, mid + 1, right)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > target or target > nums[-1]:
            return -1
        return Binsearch(nums, target, 0, len(nums))