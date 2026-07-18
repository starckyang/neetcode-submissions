class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        robbed=[0, nums[0], nums[1]]
        i=2
        n=len(nums)
        while i<n:
            robbed.append(max(robbed[i-1], robbed[i-2])+nums[i])
            i+=1
        return max(robbed[-1], robbed[-2])