class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        l, r = 0, len(height)-1
        v = 0
        c_h = min(height[r], height[l])
        v += (r-l-1) * c_h
        while l < r-1:
            if height[l] < height[r]:
                l += 1
                if height[l] > c_h:
                    v -= (c_h * (r-l))
                    c_h = min(height[r], height[l])
                    v += (r-l-1) * c_h
                else:
                    v -= height[l]
            else:
                r -= 1
                if height[r] > c_h:
                    v -= (c_h * (r-l))
                    c_h = min(height[r], height[l])
                    v += (r-l-1) * c_h
                else:
                    v -= height[r]
        return v