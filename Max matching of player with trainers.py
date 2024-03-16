class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        res=0
        i,j=0,0
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                res+=1
                i+=1
            j+=1
        return res
      
