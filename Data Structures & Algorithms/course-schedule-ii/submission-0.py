class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topology method

        hm={i:[] for i in range(numCourses)}
        counter={i:0 for i in range(numCourses)}
        ready=[]
        ans=[]
        taken=0

        for (post, pri) in prerequisites:
            hm[pri].append(post)
            counter[post]+=1

        for i in range(numCourses):
            if counter[i]==0:
                ready.append(i)

        while ready:
            cur=ready.pop()
            taken+=1
            for post in hm[cur]:
                counter[post]-=1
                if counter[post]==0:
                    ready.append(post)
            ans.append(cur)

        return ans if taken==numCourses else []