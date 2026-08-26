class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using the ord function to check if the letters are in range

        def isNumAlp(c):
            return (ord("A")<=ord(c)<=ord("Z") or 
                    ord("a")<=ord(c)<=ord("z") or 
                    ord("0")<=ord(c)<=ord("9"))

        l,r = 0,len(s)-1
        
        while l<r:
            while l<r and not isNumAlp(s[l]):
                l+=1
            while r>l and not isNumAlp(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l,r = l+1, r-1

        return True