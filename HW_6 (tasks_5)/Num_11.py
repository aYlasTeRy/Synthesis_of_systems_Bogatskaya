# https://leetcode.com/problems/make-the-string-great/
"""
Дана строка s из английских букв нижнего и верхнего регистра.
Хорошая строка - это строка, в которой нет двух смежных символов s[i] и s[i + 1]
Чтобы сделать строку хорошей, вы можете выбрать два соседних символа, которые делают строку плохой, и удалить их.
Обратите внимание, что пустая строка тоже хорошая.
"""


class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for item in s:
            if len(stack) == 0:
                stack.append(item)

            else:
                if item == item.lower():
                    if item == stack[-1].lower() and stack[-1] != item:
                        stack.pop()
                    else:
                        stack.append(item)
                elif item == item.upper():
                    if item == stack[-1].upper() and stack[-1] != item:
                        stack.pop()
                    else:
                        stack.append(item)

        return ''.join(stack)