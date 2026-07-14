import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points
        ans = []
        get_key = lambda x: -(x[0]**2 + x[1]**2)
        for i, point in enumerate(points):
            if i >= k:
                if ans[0][0] < get_key(point):
                    heapq.heappop(ans)
                    heapq.heappush(ans, (get_key(point), point))
            else:
                heapq.heappush(ans, (get_key(point), point))


        return [p[1] for p in ans]