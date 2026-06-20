class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = nums.count(i)
        result = sorted(d, key = d.get, reverse = True)[0:k]
        return result
