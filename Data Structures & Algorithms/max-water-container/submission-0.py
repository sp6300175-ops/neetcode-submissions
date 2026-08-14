class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        max_so_far = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            
            area = height * width
            max_so_far = max(area, max_so_far)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_so_far


