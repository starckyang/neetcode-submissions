class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, pass_down):
            if i >= len(nums):
                res.append(pass_down)
                return
            dfs(i+1, pass_down+[nums[i]])
            dfs(i+1, pass_down)
        dfs(0, [])
        return res