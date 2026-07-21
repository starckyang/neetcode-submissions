from heapq import heappush, heappop

class Solution:
    def minInterval(self, intervals, queries):

        intervals.sort()
        queries_sorted = sorted(enumerate(queries), key=lambda x:x[1])

        heap=[]
        ans=[-1]*len(queries)

        i=0

        for idx, q in queries_sorted:

            while i < len(intervals) and intervals[i][0] <= q:
                start,end = intervals[i]
                size=end-start+1
                heappush(heap,(size,end))
                i+=1

            while heap and heap[0][1] < q:
                heappop(heap)

            if heap:
                ans[idx]=heap[0][0]

        return ans