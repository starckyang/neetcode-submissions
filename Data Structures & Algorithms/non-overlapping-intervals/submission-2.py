class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==1:
            return 0
        intervals.sort()
        # return intervals
        count = 0
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < end:
                end = min(interval[1], end)
                count+=1
            else:
                end = interval[1]
        return count