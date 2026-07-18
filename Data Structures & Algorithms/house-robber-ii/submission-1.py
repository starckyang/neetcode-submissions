class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def max_robbed(way):
            if len(way)==1:
                return way[0]
            robbed = [0, way[0], way[1]]
            i,n=2,len(way)
            while i<n:
                robbed.append(max(robbed[i-1], robbed[i-2])+way[i])
                i+=1
            return max([robbed[-1], robbed[-2]])



        return max(max_robbed(nums[0:-1]), max_robbed(nums[1:]))