"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals==[]:
            return 0
        max_end=max([interval.end for interval in intervals])
        mp=[0]*(max_end+1)
        for interval in intervals:
            mp[interval.start]+=1
            mp[interval.end]-=1
        max_used=0
        used=0
        for ts in mp:
            used+=ts
            max_used=max_used if max_used>used else used
        return max_used
        




