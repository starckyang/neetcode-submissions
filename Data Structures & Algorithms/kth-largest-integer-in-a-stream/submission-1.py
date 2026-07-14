import heapq
import math
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = [-math.inf] * k
        for num in nums:
            self.update(num)

    def add(self, val: int) -> int:
        self.update(val)
        return self.queue[0]
            
        
    def update(self, val):
        if val > self.queue[0]:
            heapq.heappop(self.queue)
            heapq.heappush(self.queue, val)