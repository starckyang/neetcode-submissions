import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        q = []
        for stone in stones:
            heapq.heappush(q, -stone)
        while len(q) > 1:
            first = -heapq.heappop(q)
            second = -heapq.heappop(q)
            left = first-second
            if left != 0:
                heapq.heappush(q, -left)
        return 0 if not q else -q[0]