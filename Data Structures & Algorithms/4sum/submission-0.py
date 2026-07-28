class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_arr = sorted(nums)
        result = []

        for i in range(len(sorted_arr) - 1):
            if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
                continue
            num1 = sorted_arr[i]
            
            for j in range(i + 1, len(sorted_arr) - 1):
                if j > i + 1 and sorted_arr[j] == sorted_arr[j - 1]:
                    continue
                num2 = sorted_arr[j]

                left = j + 1
                right = len(sorted_arr) - 1

                while left < right:
                    current_sum = num1 + num2 + sorted_arr[left] + sorted_arr[right]

                    if current_sum == target:
                        result.append([num1, num2, sorted_arr[left] , sorted_arr[right]])
                        while left < right and sorted_arr[left] == sorted_arr[left + 1]:
                            left += 1
                        while left < right and sorted_arr[right] == sorted_arr[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    
                    elif current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1

        return result