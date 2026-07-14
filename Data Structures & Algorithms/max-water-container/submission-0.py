# A simple solution using 2-pointers
# Provides a O(n^2) solution

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, 1
        largest = 0
        for left in range(n):
            for right in range(1+left, n):
                width = right - left
                size = width * min(heights[left], heights[right])
                if size > largest:
                    largest = size
        return largest