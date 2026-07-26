class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # (conti_pos, conti_neg)
        res=nums[0]
        cur_max, cur_min=1, 1
        for num in nums:
            cur_max, cur_min=max(cur_max*num, cur_min*num, num), min(cur_max*num, cur_min*num, num)
            res=res if res>cur_max else cur_max
        return res