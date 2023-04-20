# https://leetcode.com/problems/power-of-three/submissions/936529600/
"""
Задано целое число n, верните true, если оно в степени трех. В противном случае верните false.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 3 != 0 or n <= 0:
            return False
        else:
            return self.isPowerOfThree(n // 3)