class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max=0
        res=None
        for num in nums:
            cur_max=max(cur_max+num, num)
            if res is None or cur_max>res:
                res=cur_max
        return res