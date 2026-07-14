
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        cand = []
        ht = {}
        def dfs(comb=[], i=0, csum=0):
            if csum > target:
                return
            elif csum == target:
                cand.append(sorted(comb))
                return
            else:
                while i < len(candidates):
                    dfs(comb + [(candidates[i])], i+1, csum + candidates[i])
                    i += 1
                    while (len(candidates) > i > 0) and (candidates[i] == candidates[i-1]):
                        i += 1
        dfs()
        return cand
        # return [candidates]