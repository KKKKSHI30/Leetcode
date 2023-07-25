# Priority Queue + Linked List Approach
# Time: O(n)
# Space: O(n)
# 2023.07.17: no
import heapq
class Tweet(object):
    timestamp = 0

    def __init__(self, tid):
        self.id = tid
        self.timestamp = Tweet.timestamp
        Tweet.timestamp += 1


class User(object):
    def __init__(self, uid):
        self.id = uid
        self.following = set()
        self.tweets = []
        self.following.add(uid)

    def follow(self, uid):
        if uid not in self.following:
            self.following.add(uid)

    def unfollow(self, uid):
        if uid in self.following:
            self.following.remove(uid)

    def post(self, tid):
        self.tweets.append(Tweet(tid))


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.id_to_user = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.id_to_user:
            self.id_to_user[userId] = User(userId)

        user = self.id_to_user[userId]
        user.post(tweetId)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.id_to_user:
            self.id_to_user[userId] = User(userId)

        user = self.id_to_user[userId]
        following_ids = user.following

        res = self.mergeFollowingNews(following_ids)
        return res

    def mergeFollowingNews(self, following_ids):
        heap, res, following_lists = [], [], []

        for fid in following_ids:
            fuser = self.id_to_user[fid]
            following_lists.append(fuser.tweets)

        for i, flist in enumerate(following_lists):
            if flist:
                tweet = flist[-1]
                heapq.heappush(heap, (-tweet.timestamp, i, len(flist) - 1, tweet.id))

        n = 10
        while heap and n > 0:
            n_time, outer_i, local_i, tid = heapq.heappop(heap)
            res.append(tid)  # tweet.id
            if local_i > 0:  # element index
                tweet = following_lists[outer_i][local_i - 1]
                heapq.heappush(heap, (-tweet.timestamp, outer_i, local_i - 1, tweet.id))
            n -= 1

        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.id_to_user:
            self.id_to_user[followerId] = User(followerId)

        if followeeId not in self.id_to_user:
            self.id_to_user[followeeId] = User(followeeId)

        follower = self.id_to_user[followerId]
        follower.follow(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return

        if followerId not in self.id_to_user:
            self.id_to_user[followerId] = User(followerId)

        if followeeId not in self.id_to_user:
            self.id_to_user[followeeId] = User(followeeId)

        follower = self.id_to_user[followerId]
        follower.unfollow(followeeId)