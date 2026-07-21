class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 1
        a = sorted(set(nums))
        count = 1
        if not nums:
            return 0
        for right in range(1,len(a)):
            if a[right] == a[right - 1] + 1:
                count += 1
            else:
                count = 1
            max_len = max(max_len, count)
        return max_len