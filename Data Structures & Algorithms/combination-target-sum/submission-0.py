class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(comb=[], i=0, csum=0):   
            if csum > target:
                return 
            if csum == target:
                res.append(comb)
                return
            j = i
            while j < len(nums):
                dfs(comb + [nums[j]], j, csum+nums[j])
                j += 1
        dfs()
        return res
                    

