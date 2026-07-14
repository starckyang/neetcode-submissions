## linear way

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        l, r = 0, len(heights)-1
        while l < r:
            lh, rh = heights[l], heights[r]
            v = (r-l) * min(lh, rh)
            max_v = v if v > max_v else max_v
            if lh > rh:
                r -= 1
            else:
                l += 1
        return max_v