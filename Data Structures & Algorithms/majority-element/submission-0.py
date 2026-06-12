class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums)
        for i in s:
            if nums.count(i) > n//2:
                return i
        

