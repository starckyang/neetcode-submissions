class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        res=0
        while l<r:
            res=max(res, min(heights[r], heights[l])*(r-l))
            if heights[l]<heights[r]:
                cur_height=heights[l]
                while l<r and heights[l]<=cur_height:
                    l+=1
            else:
                cur_height=heights[r]
                while r>l and heights[r]<=cur_height:
                    r-=1
        return res