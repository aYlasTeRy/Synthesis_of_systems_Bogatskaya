#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/945124880/

"""
Существует массив целых чисел, nums отсортированных в порядке возрастания (с различными значениями).

Перед передачей вашей функции он, nums возможно, поворачивается с неизвестным сводным индексом k (1 <= k < nums.length)
таким образом, что результирующий массив имеет [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-индексированный).
Например, [0,1,2,4,5,6,7] может быть повернут по сводному индексу 3 и стать [4,5,6,7,0,1,2].

Учитывая массив nums после возможного поворота и целое число target,
верните индекс target, если он находится в nums или -1 если его нет в nums.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid

            else:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        else:
            return -1
