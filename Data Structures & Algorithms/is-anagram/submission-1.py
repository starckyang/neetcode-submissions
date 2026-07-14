class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = [0] * 26
        for char in s:
            char_count[ord(char)-ord("a")] += 1
        for char in t:
            char_count[ord(char)-ord("a")] -= 1
        
        return all(c==0 for c in char_count)