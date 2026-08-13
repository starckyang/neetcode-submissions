class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        hm={}
        def dfs(i,csum):
            if i==len(nums):
                return csum==target
            if (i, csum) in hm:
                return hm[(i, csum)]
            ways=dfs(i+1, csum-nums[i])+dfs(i+1, csum+nums[i])
            hm[(i, csum)]=ways
            return ways

        return dfs(0,0)

        