class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sorted_arr = sorted(nums)
        lst = []

        for i in range(0,len(sorted_arr) - 2 ):
            if i > 0 and sorted_arr[i] == sorted_arr[i-1]:
                continue
            num1 = sorted_arr[i]

            left = i + 1
            right = len(sorted_arr) - 1


            while left < right:
                if sorted_arr[left] + sorted_arr[right] == -num1:
                    lst.append([num1, sorted_arr[left], sorted_arr[right]])
                    while left < right and sorted_arr[left] == sorted_arr[left+1]:
                        left += 1
                    while left < right and sorted_arr[right] == sorted_arr[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sorted_arr[left] + sorted_arr[right] > -num1:
                    right -= 1
                elif sorted_arr[left] + sorted_arr[right] < -num1:
                    left += 1
        return lst
