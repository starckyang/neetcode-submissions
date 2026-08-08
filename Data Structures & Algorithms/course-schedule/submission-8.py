class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre=[[] for _ in range(numCourses)]
        for prep in prerequisites:
            pre[prep[0]].append(prep[1])

        # find the loop
        def dfs(t, been):
            been[t]=True
            for c in pre[t]:
                if c in been and been[c]:
                    return True
            for c in pre[t]:
                if dfs(c, been):
                    return True
            been[t]=False
            pre[t]=[]
            return False

        for i in range(numCourses):
            if dfs(i, {}):
                return False
        return True


        