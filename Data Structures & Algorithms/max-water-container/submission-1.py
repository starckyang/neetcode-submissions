# two pointers solution2
# if a smaller than previous, pass

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_volume = 0
        max_left = 0
        for left in range(n):
            max_right = 0
            if heights[left] > max_left:
                max_left = heights[left]
                for right in range(n-1, left, -1):
                    if heights[right] > max_right:
                        max_right = heights[right]
                        width = right - left
                        volume = width * min(max_right, max_left)
                        max_volume = volume if volume > max_volume else max_volume
        return max_volume
