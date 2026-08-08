from collections import deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        # stack
        l=deque([])
        st=deque([])
        for i, c in enumerate(s):
            if c == "(":
                l.append(i)
            elif c == "*":
                st.append(i)
            else:
                if len(l)>0:
                    l.pop()
                elif len(st)>0:
                    st.pop()
                else:
                    return False
        if len(l)>len(s):
            return False
        for lp in l:
            while st and lp > st[0]:
                st.popleft()
            if st:
                st.popleft()
            else:
                return False
        return True






