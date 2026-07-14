class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        nzeros = 0
        for num in nums:
            if num == 0:
                nzeros += 1
            else:
                pro *= num
        res = []
        if nzeros > 1:
            res = [0] * len(nums)
        elif nzeros == 1:
            res = [0 if nums[i] != 0 else int(pro) for i in range(len(nums)) ]
        else:
            res = [int(pro/nums[i]) for i in range(len(nums))]
        return res