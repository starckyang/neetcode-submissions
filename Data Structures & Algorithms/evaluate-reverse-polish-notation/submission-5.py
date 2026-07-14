class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        ops = {"+": True, "-": True, "*": True, "/": True}
        for tok in tokens:
            if tok not in ops:
                num_stack.append(int(tok))
            else:
                b = num_stack.pop()
                a = num_stack.pop()
                if tok == "+":
                    num_stack.append(a + b)
                if tok == "-":
                    num_stack.append(a - b)
                if tok == "*":
                    num_stack.append(a * b)
                if tok == "/":
                    num_stack.append(int(a/b))
        return num_stack[-1]