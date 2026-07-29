class Twitter:

    def __init__(self):
        self.user_follows = dict()
        self.user_posts = dict()
        self.global_posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_posts.keys():
            self.user_posts[userId] = [tweetId]
        else:
            self.user_posts[userId].append(tweetId)
        self.global_posts.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        if userId not in self.user_follows.keys():
            self.user_follows[userId] = [userId]
        nb_posts = len(self.global_posts)
        for i in range(nb_posts - 1, -1, -1):
            poster = self.global_posts[i][0]
            postId = self.global_posts[i][1]
            if poster in self.user_follows[userId] or poster == userId:
                feed.append(postId)
        return feed[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follows.keys():
            self.user_follows[followerId] = [followerId, followeeId]
        elif followeeId not in self.user_follows[followerId]:
            self.user_follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId not in self.user_follows.keys() or
                followeeId not in self.user_follows[followerId]):
            return
        else:
            self.user_follows[followerId].remove(followeeId)
