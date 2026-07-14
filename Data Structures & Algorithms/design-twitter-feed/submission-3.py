import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.ugc = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.initiation(userId)
        self.ugc[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        self.initiation(userId)
        feed = []
        for followee in self.following[userId]:
            for content in self.ugc[followee]:
                if len(feed) >= 10:
                    if feed[0][0] < content[0]:
                        heapq.heappop(feed)
                        heapq.heappush(feed, content)
                else:
                    heapq.heappush(feed, content)
        return [content[1] for content in sorted(feed, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.initiation(followerId)
        self.initiation(followeeId)
        if not followeeId in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.initiation(followerId)
        self.initiation(followeeId)
        if (followeeId in self.following[followerId]) and (followeeId != followerId):
            self.following[followerId].remove(followeeId)


    def initiation(self, userId):
        if not userId in self.ugc:
            self.ugc[userId] = [] 
            self.following[userId] = [userId]