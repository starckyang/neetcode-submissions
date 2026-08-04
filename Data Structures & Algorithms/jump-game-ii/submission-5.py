class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        memo=[False]*len(nums)
        def dfs(idx):
            if (idx+1)>=len(nums):
                return 0
            max_reach=idx
            next_ind=idx
            for step in range(1, min([nums[idx]+1, len(nums)-idx])):
                if memo[idx+step]==True:
                    continue
                if idx+step+nums[idx+step]>=max_reach:
                    memo[idx+step]=True
                    max_reach=idx+step+nums[idx+step]
                    next_ind=idx+step
                if idx+step+1>=len(nums):
                    return 1
            return dfs(next_ind)+1
        return dfs(0)