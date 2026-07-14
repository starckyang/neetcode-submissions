class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hm = {s[0]: 1}
        res = 0
        while r < len(s):
        
            big, others = 0, 0
            for (key, value) in hm.items():
                if value > big:
                    others = others + big
                    big = value
                else:
                    others += value
            
            if others > k:
                hm[s[l]] -= 1
                l += 1
            else:
                res = (r-l+1) if (r-l+1) > res else res
                r += 1
                if r == len(s):
                    break
                if s[r] in hm:
                    hm[s[r]] += 1
                else:
                    hm[s[r]] = 1
        return res