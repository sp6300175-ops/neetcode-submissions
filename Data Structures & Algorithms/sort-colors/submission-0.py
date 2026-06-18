class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = []
        for i in [0,1,2]:
            if i in nums:
                Count = nums.count(i)
                for j in range(Count):
                    l.append(i)
        nums[:] = l

