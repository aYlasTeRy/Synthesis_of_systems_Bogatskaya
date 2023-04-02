# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
"""
Вам выдается строка s, состоящая из строчных английских букв.
Удаление дубликатов состоит в выборе двух соседних и равных букв
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for item in s:
            if item not in stack:
                stack.append(item)
            else:
                if item == stack[-1]:
                    stack.pop()
                else:
                    stack.append(item)

        return ''.join(stack)