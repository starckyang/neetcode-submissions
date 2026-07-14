class Solution:
    def isValid(self, s: str) -> bool:
        open_d, close_d = {par: True for par in ['(', '[', '{']}, {'}': '{', ')': '(', ']': '['}
        stack = list()
        for char in s:
            if char in open_d:
                stack.append(char)
            else:
                if not stack or stack[-1] != close_d[char]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False