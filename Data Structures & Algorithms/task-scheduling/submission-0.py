import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for alph in tasks:
            if alph in count:
                count[alph] += 1
            else:
                count[alph] = 1
        
        stack = []
        for (key, val) in count.items():
            heapq.heappush(stack, (-val, key))
        
        rest = []
        rounds = 0
        while stack or rest:
            rounds += 1
            for cand in rest:
                cand[0] -= 1
            if rest and (rest[0][0] == 0):
                _, cnt, alph = heapq.heappop(rest)
                heapq.heappush(stack, (-cnt, alph))
            if stack:
                cnt, alph = heapq.heappop(stack)
                cnt = -cnt
                cnt-=1
                if cnt > 0:
                    heapq.heappush(rest, [n+1, cnt, alph])
            
        return rounds