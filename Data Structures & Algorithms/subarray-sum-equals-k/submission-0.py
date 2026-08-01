class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mark = {0:1}
        running_total = 0
        answer_count = 0

        for i in nums:
            running_total += i
            
            if running_total - k in mark:
                answer_count += mark[running_total - k]

            mark[running_total] = mark.get(running_total, 0) + 1
            
        return answer_count