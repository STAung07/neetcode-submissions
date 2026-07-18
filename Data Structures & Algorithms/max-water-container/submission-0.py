class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(heights) - 1
        max_water = 0

        while (left_ptr < right_ptr):
            max_water = max(min(heights[left_ptr], heights[right_ptr]) * (right_ptr - left_ptr), max_water)
            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        
        return max_water
            
            