class Twitter:

    def __init__(self):
        self.tweets = []
        heapq.heapify(self.tweets)
        self.users = defaultdict(set)
        self.num_posts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        print(f'User {userId} posted tweet {tweetId} with num posts = {self.num_posts}')
        heapq.heappush(self.tweets, (-self.num_posts, userId, tweetId))
        self.num_posts += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        found = 0
        while self.tweets:
            if found == 10:
                break
            tweet = heapq.heappop(self.tweets)
            if tweet[1] in self.users[userId] or tweet[1] == userId:
                found += 1
            feed.append(tweet)
        for tweet in feed:
            heapq.heappush(self.tweets, tweet)
        return [ tweet[2] for tweet in feed if tweet[1] in self.users[userId] or tweet[1] == userId ]

    def follow(self, followerId: int, followeeId: int) -> None:
        print(f'User {followerId} followed user {followeeId}')
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(f'User {followerId} unfollowed user {followeeId}')
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)