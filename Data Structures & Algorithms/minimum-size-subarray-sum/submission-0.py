class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_so_far = float('inf')
        current_sum = 0

        for right in range(0, len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                current_sum -= nums[left]
                min_so_far = min(min_so_far, right - left + 1)
                left += 1
        if min_so_far == float('inf'):
            return 0
        else:      
            return min_so_far 
