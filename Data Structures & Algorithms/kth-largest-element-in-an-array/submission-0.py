import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_large = []
        for i, num in enumerate(nums):
            if i >= k:
                if k_large[0] < num:
                    heapq.heappop(k_large)
                    heapq.heappush(k_large,num)
            else:
                heapq.heappush(k_large, num)
        return k_large[0]