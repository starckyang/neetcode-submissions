class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        miss = {}
        for i, num in enumerate(nums):
            if num in miss:
                return [miss[num], i]
            miss[target-num] = i
        return False