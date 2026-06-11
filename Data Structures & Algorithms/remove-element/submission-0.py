class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        times = nums.count(val)
        for i in range (times):
            nums.remove(val)
        return len(nums)