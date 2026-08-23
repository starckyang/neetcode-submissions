class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={')':'(', '}':'{', ']':'['}

        for char in s:
            if char in set(["[", "{", "("]):
                stack.append(char)
            elif char in set(["]", "}", ")"]):
                if stack and stack[-1]==match[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if stack:
            return False
        
        return True