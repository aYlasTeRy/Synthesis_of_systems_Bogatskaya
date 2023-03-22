# https://leetcode.com/problems/intersection-of-two-arrays/


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = 0
        l2 = 0
        nums3 = []
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        for l1 in nums1:
            for l2 in nums2:
                if l1 == l2 and l1 not in nums3:
                    nums3.append(l1)

        return nums3