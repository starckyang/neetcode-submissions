import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        hm=defaultdict(int)
        for num in nums:
            hm[num]+=1
        
        for key, value in hm.items():
            if len(res)<k:
                heapq.heappush(res, [value, key])
            else:
                if value>res[0][0]:
                    heapq.heappop(res)
                    heapq.heappush(res, [value, key])
        
        return [rec[1] for rec in res]
            
