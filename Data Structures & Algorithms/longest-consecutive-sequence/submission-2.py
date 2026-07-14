class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {num: True for num in nums}
        max_cons = 0
        for num in nums:
            cur_cnt = 1
            cur_num = num
            if not num-1 in nums_dict:
                while cur_num+1 in nums_dict:
                    cur_cnt += 1
                    cur_num += 1
            max_cons = cur_cnt if cur_cnt > max_cons else max_cons
        return max_cons