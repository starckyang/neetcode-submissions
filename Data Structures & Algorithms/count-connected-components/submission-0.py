from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tracker=set()
        counter=0
        hm={i:[] for i in range(n)}
        for edge in edges:
            hm[edge[0]].append(edge[1])
            hm[edge[1]].append(edge[0])

        def dfs(i):
            tracker.add(i)
            for nb in hm[i]:
                if not nb in tracker:
                    dfs(nb)
                
        for t in range(n):
            if not t in tracker:
                counter+=1
                dfs(t)
        
        return counter