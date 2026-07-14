class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(comb, hm):
            comb = comb.copy()
            if len(comb) == len(nums):
                res.append(comb)
                return
            for num in nums:
                if not num in hm:
                    comb.append(num)
                    hm[num] = True
                    dfs(comb, hm)
                    comb.pop()
                    del hm[num]
        dfs([],{})
        return res