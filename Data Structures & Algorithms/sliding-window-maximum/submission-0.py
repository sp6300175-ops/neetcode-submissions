
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        result = []
        left = 0
        for right in range(0, len(nums)):
            while d and nums[d[-1]] < nums[right]:
                d.pop()
            d.append(right)
            if d[0] < left:
                d.popleft()
            if right - left + 1 == k:
                result.append(nums[d[0]]) 
                left += 1
        return result
                