class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()

        p, t = 0, 0
        matchings = 0

        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                matchings += 1
                p += 1
            t += 1

        return matchings