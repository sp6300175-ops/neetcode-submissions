from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)

        while start < end:
            mid = (start + end) // 2
            if self.hours_needed(piles, mid) <= h:
                end = mid
            else:
                start = mid + 1
        return start




    def hours_needed(self, piles, k):
        total = 0

        for pile in piles:
            hours = ceil(pile / k)
            total += hours
        return total

