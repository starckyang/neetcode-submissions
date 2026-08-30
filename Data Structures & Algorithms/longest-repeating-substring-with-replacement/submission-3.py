class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        c_max=0
        l=0

        for r, c in enumerate(s):
            count[c] = count.get(c)+1 if count.get(c) else 1
            c_max = max(c_max, count[c])
            while (r-l+1-c_max)>k:
                count[s[l]]-=1
                l+=1
            res=max(res, r-l+1)

        return res