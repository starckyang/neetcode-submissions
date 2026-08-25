class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack=[]
        loc_stack=[]
        res=[0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while temp_stack and temp_stack[-1]<temp:
                temp_stack.pop()
                loc=loc_stack.pop()
                res[loc]=i-loc
            temp_stack.append(temp)
            loc_stack.append(i)
        
        return res