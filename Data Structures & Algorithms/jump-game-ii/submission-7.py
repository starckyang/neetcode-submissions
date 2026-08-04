class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        l=r=0
        while r<len(nums)-1:
            res+=1
            cur_max=r
            for i in range(l, r+1):
                if i+nums[i]>cur_max:
                    cur_max=i+nums[i]
            l=r+1
            r=cur_max
        return res