from collections import deque
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        max_end=max([interval[1] for interval in intervals])
        min_map=[-1]*(max_end+1)
        intervals.sort()
        stack=deque([])
        int_pt=0
        for i in range(max_end+1):
            while stack and stack[0][0]<i:
                    stack.popleft()

            while int_pt < len(intervals) and intervals[int_pt][0]==i:
                end=intervals[int_pt][1]
                rg=end-intervals[int_pt][0]+1
                temp=[]
                while stack and stack[-1][1]>rg:
                    temp.append(stack.pop())
                if (not stack) or (stack and end>stack[-1][0]):
                    stack.append([end, rg])
                while temp:
                    t_end, t_rg=temp.pop()
                    if t_end>end:
                        stack.append([t_end, t_rg])
                int_pt+=1
            if stack:
                min_map[i]=stack[0][1]

        res=[]
        for query in queries:
            if query<0 or query>max_end:
                res.append(-1)
            else:
                res.append(min_map[query])
            
        return res
