class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # method2: greedy
        i=0
        visited=[False]*len(nums)
        while i<len(nums):
            jump=nums[i]
            if (i+jump+1) >= len(nums):
                return True
            cur_max=0
            next_pos=i
            for step in range(1, jump+1):
                if visited[step]:
                    continue
                reach=step+nums[i+step]
                if reach>cur_max:
                    cur_max=max(cur_max, reach)
                    next_pos=i+step
            if next_pos==i:
                return False
            i=next_pos
            