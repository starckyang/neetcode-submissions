class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)>h:
            return -1
        l,r=1,max(piles)

        while l<r:
            m=(l+r)//2
            hrs=0
            for pile in piles:
                hrs+=(pile//m if pile%m==0 else pile//m+1)
            if hrs>h:
                l=m+1
            else:
                r=m

        return r
