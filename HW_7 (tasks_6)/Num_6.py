# https://leetcode.com/problems/first-bad-version/
"""

"""

def Binsearch(left, right):
    mid = (left + right) // 2
    if left > right:
        return left
    if isBadVersion(mid):
        return Binsearch(left, mid - 1)
    else:
        return Binsearch(mid + 1, right)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        return Binsearch(1, n)