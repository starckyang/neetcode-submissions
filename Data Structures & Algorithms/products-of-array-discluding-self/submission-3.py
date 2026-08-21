class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # non-division

        left=[1]*len(nums)
        right=[1]*len(nums)

        for i in range(len(nums)-1):
            left[i+1]=left[i]*nums[i]
            right[len(nums)-2-i]=right[len(nums)-1-i]*nums[len(nums)-1-i]

        res=[]
        for i in range(len(nums)):
            res.append(left[i]*right[i])

        return res