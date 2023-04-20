# https://leetcode.com/problems/reverse-string/submissions/937120481/
"""
Напишите функцию, которая переворачивает строку. Входная строка задается в виде массива символов s.
"""

def reverse(s, left, right):
    if left > right:
        return s
    s[left], s[right] = s[right], s[left]
    return reverse(s, left + 1, right - 1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        return reverse(s, 0, len(s) - 1)