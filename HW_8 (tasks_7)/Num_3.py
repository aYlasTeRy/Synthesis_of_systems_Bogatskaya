# https://leetcode.com/problems/minimum-time-to-repair-cars/
"""
Вам предоставляется целочисленный массив, ranks представляющий ранги некоторых механиков.
Механик с рангом r может ремонтировать n автомобили за r * n2 минуты.
Вам также предоставляется целое число, cars представляющее общее количество автомобилей, ожидающих ремонта в гараже.
Верните минимальное время, затраченное на ремонт всех автомобилей.
Примечание: Все механики могут ремонтировать автомобили одновременно.
"""
from math import sqrt, ceil

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        l = 0
        r = min(ranks) * (cars ** 2)

        while l < r:

            mid = (l + r) // 2
            count = 0

            for rank in ranks:
                count += floor(sqrt(mid / rank))
                # count += math.floor((mid / rank) ** 0.5)

            if count < cars:
                l = mid + 1
            else:
                r = mid

        return l