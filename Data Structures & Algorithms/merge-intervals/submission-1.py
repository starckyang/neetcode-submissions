class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        n=len(intervals)
        prev=intervals[0]
        res = []
        while i<n:
            if prev[1]>=intervals[i][0]:
                prev = [
                    min(prev[0], intervals[i][0]),
                    max(prev[1], intervals[i][1])
                ]
            else:
                res.append(prev)
                prev=intervals[i]
            i+=1

        res.append(prev)
        return res