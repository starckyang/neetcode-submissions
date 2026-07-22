class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len=1
        max_pal=s[0]

        for i in range(len(s)):
            # even
            left=i-1
            right=i
            while left>-1 and right<len(s):
                if s[left]==s[right]:
                    left, right=left-1, right+1
                else:
                    break
            if right-left-1>max_len:
                max_len=right-left-1
                max_pal=s[left+1:right]
            
            # odd
            left=i-1
            right=i+1
            while left>-1 and right<len(s):
                if s[left]==s[right]:
                    left, right=left-1, right+1
                else:
                    break
            if right-left-1>max_len:
                max_len=right-left-1
                max_pal=s[left+1:right]

        return max_pal  