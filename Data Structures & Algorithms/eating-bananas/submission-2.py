import math


class Solution:
    def get_eat_time(self, piles: List[int], k: int) -> int:
        time = 0
        for value in piles:
            time += math.ceil(value / k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_bound = 1
        max_bound = max(piles)
        while min_bound != max_bound:
            middle = (max_bound + min_bound) // 2
            if self.get_eat_time(piles, middle) > h:
                min_bound = middle + 1
            else:
                max_bound = middle
        return min_bound
