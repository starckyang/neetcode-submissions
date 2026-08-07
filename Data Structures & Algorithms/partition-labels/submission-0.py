class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        hm={}
        for i, char in enumerate(s):
            hm[char]=i

        l, r, t = 0, 0, 0
        res=[]
        while l<len(s):
            c = s[l]
            r = hm[c]
            t = l
            while t<=r:
                r=max(hm[s[t]], r)
                t+=1
            res.append(r-l+1)
            l=r+1
        return res