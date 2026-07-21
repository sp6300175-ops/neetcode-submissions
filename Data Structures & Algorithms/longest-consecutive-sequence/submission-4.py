class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        max_len = 1
        if not nums:
            return 0
        for i in range(len(nums)) :
            if nums[i] - 1 not in a:
                count = 1
                current = nums[i]
                while current + 1 in a:   
                    count += 1
                    current += 1
                max_len = max(max_len, count)
        return max_len
