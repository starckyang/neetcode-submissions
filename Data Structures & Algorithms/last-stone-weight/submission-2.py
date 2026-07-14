import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()
            left = abs(first-second)
            if left != 0:
                heapq.heappush(stones, left)
        return 0 if not stones else stones[0]