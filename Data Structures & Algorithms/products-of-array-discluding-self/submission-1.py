class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_pro = {}
        right_pro = {}
        for i in range(len(nums)):
            if i == 0:
                left_pro[i] = nums[i]
                right_pro[len(nums)-1] = nums[len(nums)-1]
            else:
                left_pro[i] = left_pro[i-1] * nums[i]
                right_pro[len(nums)-1-i] = right_pro[len(nums)-i] * nums[len(nums)-1-i]
        left_pro[-1], right_pro[len(nums)] = 1, 1 

        res = [left_pro[i-1] * right_pro[i+1] for i in range(len(nums))]
        return res
        