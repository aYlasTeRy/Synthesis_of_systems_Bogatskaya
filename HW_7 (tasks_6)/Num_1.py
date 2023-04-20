# https://leetcode.com/problems/fibonacci-number/submissions/936523731/
"""
Числа Фибоначчи, обычно обозначаемые F(n), образуют последовательность,
называемую последовательностью Фибоначчи, такую, что каждое число является суммой двух предыдущих, начиная с 0 и 1.
Посчитайте F(n)
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)