# https://leetcode.com/problems/valid-parentheses/
"""
Учитывая строку, s содержащую только символы '(', ')', '{', '}''[', ']'
определите, является ли входная строка допустимой.
Строка ввода допустима, если:
Открытые скобки должны быть закрыты скобками того же типа.
Открытые скобки должны быть закрыты в правильном порядке.
Каждой закрывающей скобке соответствует открывающая скобка того же типа.
"""


class Solution:
    def isValid(self, s: str) -> bool:

        data = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []

        for item in s:
            if item in data:
                stack.append(item)
            else:
                if len(stack) == 0 or data[stack.pop()] != item:
                    return False

        if len(stack) > 0:
            return False

        return True
