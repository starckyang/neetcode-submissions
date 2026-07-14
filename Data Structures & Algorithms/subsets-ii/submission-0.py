class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:       
        nums = sorted(nums)
        res = []

        def dfs(comb=[], used=[0] * len(nums), i=0):
            res.append(comb.copy())

            while i < len(nums):
                if (i > 0) and (nums[i] == nums[i-1]) and (used[i-1] == 0):
                    pass
                else:
                    comb.append(nums[i])
                    used[i] = 1
                    dfs(comb, used, i+1)
                    comb.pop()
                    used[i] = 0
                i+=1

        dfs()
        return res