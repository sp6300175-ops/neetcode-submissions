class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2 
            if self.days_needed(weights, mid) <= days:
                high = mid
            else:
                low = mid + 1
        return low

    def days_needed(self, weights, capacity):
        days = 1
        current_load = 0

        for wt in weights:
            if current_load + wt > capacity:
                days += 1
                current_load = 0
            current_load += wt
        
        return days