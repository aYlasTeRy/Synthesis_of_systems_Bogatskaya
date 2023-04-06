# https://leetcode.com/problems/remove-outermost-parentheses/description/
"""
Input: s = "(()())(())"
Output: "()()()"
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        counter = 0

        for item in s:
            if item == "(":
                if counter != 0:
                    stack.append(item)
                counter += 1
            else:
                counter -= 1
                if counter != 0:
                    stack.append(item)

        return ''.join(stack)