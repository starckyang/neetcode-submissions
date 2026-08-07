class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res=[0, 0, 0]
        ta, tb, tc=target
        for a, b, c in triplets:
            if (a<=ta)&(b<=tb)&(c<=tc):
                res=[max(res[0], a), max(res[1], b), max(res[2], c)]
            if res==target:
                return True
        return False