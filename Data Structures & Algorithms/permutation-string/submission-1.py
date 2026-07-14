class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_q = {}
        s2_q = {}
        for char in s1:
            if char in s1_q:
                s1_q[char] += 1
            else:
                s1_q[char] = 1
        right = 0
        for i in range(len(s2)-len(s1)+1):
            while right < (len(s1)+i):
                if s2[right] in s2_q:
                    s2_q[s2[right]] += 1
                else:
                    s2_q[s2[right]] = 1
                right += 1
            if s1_q == s2_q:
                return True
            s2_q[s2[i]] -= 1
            if s2_q[s2[i]] == 0:
                del s2_q[s2[i]]
        return False