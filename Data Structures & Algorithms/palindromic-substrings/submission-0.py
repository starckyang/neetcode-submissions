class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt=0
        def check_pal(l, r, cnt):
            if l<0 or r>=len(s):
                return cnt
            if s[l]==s[r]:
                cnt+=1
                return check_pal(l-1, r+1, cnt)
            return cnt
        for i, c in enumerate(s):
            cnt+=1
            cnt=check_pal(i, i+1, cnt)
            cnt=check_pal(i-1, i+1, cnt)

        return cnt

