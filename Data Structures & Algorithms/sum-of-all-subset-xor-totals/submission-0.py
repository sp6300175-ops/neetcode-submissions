class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_sum = 0
        for num in nums:
            or_sum |= num
        return or_sum * (1 << (len(nums) - 1)) 