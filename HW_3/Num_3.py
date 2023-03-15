# https://leetcode.com/problems/valid-palindrome-ii/

def palindrom(data, l, r):
    while l < r:
        if data[l] != data[r]:
            return False
        l += 1
        r -= 1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return palindrom(s, l + 1, r) or palindrom(s, l, r - 1)
            l += 1
            r -= 1
        return True