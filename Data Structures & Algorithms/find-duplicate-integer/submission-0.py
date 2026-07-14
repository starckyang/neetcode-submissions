class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. space O(n) hash map solution
        hm = {}
        for num in nums:
            if num in hm:
                return num
            else:
                hm[num] = True
        return False