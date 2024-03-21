class Twitter:

    def __init__(self):
        self.tweetslist=[]
        self.followers={}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetslist.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        lst=[]
        for i in range(len(self.tweetslist) -1,-1,-1):
            if self.tweetslist[i][0]==userId:
                lst.append(self.tweetslist[i][1])
                if len(lst)==10:
                    break;
            else:
                if userId in self.followers:
                    val=self.followers[userId]
                    if self.tweetslist[i][0] in val:
                        lst.append(self.tweetslist[i][1])
                        if len(lst)==10:
                            break;
        return lst       

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            val=self.followers[followerId]
            val.append(followeeId)
            self.followers[followerId]=val
        else:
            lst=[followeeId]
            self.followers[followerId]=lst

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            val=self.followers[followerId]
            val.remove(followeeId)
            self.followers[followerId]=val
