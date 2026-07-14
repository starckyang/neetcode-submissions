class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = nums[0], nums[0]
        start = False
        while (s != f) or (not start):
            start = True
            s = nums[s]
            f = nums[nums[f]]

        s = nums[0]
        while s != f:
            s, f = nums[s], nums[f]

        return s