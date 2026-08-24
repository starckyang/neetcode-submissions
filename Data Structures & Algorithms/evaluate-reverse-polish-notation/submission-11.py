class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token=tokens.pop()
            if token not in ("+", "-", "*", "/"):
                return int(token)
            
            right=dfs()
            left=dfs()

            if token=="+":
                return left+right
            if token=="-":
                return left-right
            if token=="*":
                return left*right
            if token=="/":
                if left*right<0:
                    return -int(abs(left/right))
                return int(left/right)

        return dfs()

