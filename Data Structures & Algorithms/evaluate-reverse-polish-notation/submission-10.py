class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack=[]
        for token in tokens:
            if token.isnumeric() or (len(token)>1 and token[1:].isnumeric()):
                num_stack.append(int(token))
            else:
                a=num_stack.pop()
                b=num_stack.pop()
                if token=="+":
                    num_stack.append(a+b)
                if token=="-":
                    num_stack.append(b-a)
                if token=="*":
                    num_stack.append(a*b)
                if token=="/":
                    num_stack.append(((a*b)/abs(a*b))*int(abs(b/a)) if a*b!=0 else 0)
        return int(num_stack[-1])