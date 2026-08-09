class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        hm={i:[] for i in range(n)}
        for n1, n2 in edges:
            hm[n1].append(n2)
            hm[n2].append(n1)
        ttl={}

        def dfs(i,visited={},prev=None):
            visited[i]=True
            if not i in ttl:
                ttl[i]=True
            for node in hm[i]:
                if (prev is not None) and (node == prev):
                    continue
                elif node in visited:
                    return True
                else:
                    if dfs(node, visited, i):
                        return True
            return False

        return (not dfs(0)) and (len(ttl)==n)