# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l1 = 0
        l2 = len(nums) - 1
        while l1 <= l2:
            if nums[l1] == val and nums[l2] != val:
                nums[l1], nums[l2] = nums[l2], nums[l1]
                l1 += 1
                l2 -= 1
            elif nums[l1] == val and nums[l2] == val:
                l2 -= 1
            elif nums[l1] != val:
                l1 += 1


        return l1