class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_q = {}
        for char in t:
            if char in t_q:
                t_q[char] += 1
            else:
                t_q[char] = 1

        l, r = 0, 0
        shortest_len = None
        best_lr = None
        rec = []
        while r < len(s):
            if s[r] in t_q:
                t_q[s[r]] -= 1

            while l <= r:
                if s[l] not in t_q:
                    l += 1
                elif t_q[s[l]] < 0:
                    t_q[s[l]] += 1
                    l += 1
                else:
                    break

            done = True
            for key, value in t_q.items():
                if value > 0:
                    done = False

            if done:
                if (shortest_len == None) or (shortest_len > (r-l)):
                    shortest_len = r-l
                    best_lr = (l, r)
                
            r += 1

        return "" if not best_lr else s[best_lr[0]:best_lr[1]+1]