# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
"""
Учитывая, что VPS представлен в виде строки s, верните глубину вложенности s.
"""


class Solution:
    def maxDepth(self, s: str) -> int:

        data = {"(": ")"}
        stack = []
        max_len_stack = 0

        for item in s:
            if item in data:
                stack.append(item)
                if len(stack) > max_len_stack:
                    max_len_stack = len(stack)

            else:
                if item == ")":
                    stack.pop()

        return max_len_stack