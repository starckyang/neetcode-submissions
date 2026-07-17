class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval

        for i, (c_start, c_end) in enumerate(intervals):
            if c_end >= start:
                start = min(start, c_start)
            if c_start <= end:
                end = max(end, c_end)
    
        res = []
        inserted = False
        for i, (c_start, c_end) in enumerate(intervals):
            if c_start >= start and c_end <= end:
                continue
            elif c_start > end and inserted is False:
                res.append([start, end])
                res.append([c_start, c_end])
                inserted = True
            else:
                res.append([c_start, c_end])
        
        if inserted is False:
            res.append([start, end])

        return res