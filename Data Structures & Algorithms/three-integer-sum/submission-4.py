class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            tar=-nums[i]
            hm=set()
            for j in range(i+1, len(nums)):
                if tar-nums[j] in hm:
                    res.append((-tar, nums[j], tar-nums[j]))
                hm.add(nums[j])
        
        return list(set(res))