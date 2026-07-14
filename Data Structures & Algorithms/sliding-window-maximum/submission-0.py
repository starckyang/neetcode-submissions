from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def insert_monotone_queue(vq, idq, val, idx):
            while (vq) and (vq[-1] < val):
                val_q.pop()
                idx_q.pop()
            val_q.append(nums[idx])
            idx_q.append(idx)
            return val_q, idx_q
            
        val_q = deque()
        idx_q = deque()
        res = []
        for i in range(len(nums)-k+1):
            if i == 0:
                for j in range(k-1):
                    val_q, idx_q = insert_monotone_queue(val_q, idx_q, nums[j], j)
            if (idx_q) and (idx_q[0] < i):
                val_q.popleft()
                idx_q.popleft()
            val_q, idx_q = insert_monotone_queue(val_q, idx_q, nums[(i+k-1)], (i+k-1))
            res.append(val_q[0])

        return res

                    