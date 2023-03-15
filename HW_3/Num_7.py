# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1
        while l < r:
            t = s[l]
            s[l] = s[r]
            s[r] = t
            l += 1
            r -= 1
        return s