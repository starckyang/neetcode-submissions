class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            mid_n = nums[mid]
            if mid_n == target:
                return mid
            elif mid_n < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1