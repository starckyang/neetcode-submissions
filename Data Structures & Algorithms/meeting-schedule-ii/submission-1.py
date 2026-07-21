"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        intervals = sorted(intervals, key=lambda interval:[interval.start, interval.end])
        stack=[]
        max_con=0
        for interval in intervals:
            while stack and stack[0]<=interval.start:
                heapq.heappop(stack)
            heapq.heappush(stack, interval.end)
            if len(stack)>max_con:
                max_con=len(stack)
        return max_con