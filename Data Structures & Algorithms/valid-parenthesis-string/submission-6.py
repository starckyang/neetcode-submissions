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
        while l and st:
            if l.pop() > st.pop():
                return False
        if l:
            return False
        return True






