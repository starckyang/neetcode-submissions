import heapq
class MedianFinder:

    def __init__(self):
        self.top = []
        self.bot = []

    def addNum(self, num: int) -> None:
        if len(self.top) == len(self.bot):
            if (not self.top) or (-self.bot[0] < num):
                heapq.heappush(self.top, num)
            else:
                move = -heapq.heappop(self.bot)
                heapq.heappush(self.top, move)
                heapq.heappush(self.bot, -num)
        else:
            if self.top[0] < num:
                move = heapq.heappop(self.top)
                heapq.heappush(self.top, num)
                heapq.heappush(self.bot, -move)
            else:
                heapq.heappush(self.bot, -num)

    def findMedian(self) -> float:
        if len(self.top) == len(self.bot):
            return (self.top[0] - self.bot[0])/2
        return self.top[0]
        