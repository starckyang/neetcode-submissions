"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start))

        max_end = 0
        for interval in intervals:
            if max_end > interval.start:
                return False
            else:
                max_end = max_end if interval.end < max_end else interval.end

        return True