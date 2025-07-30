class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        s_players = sorted(players)
        s_trainers = sorted(trainers)

        ans = 0
        p1,p2 = len(players) - 1, len(trainers) - 1
        while p1 >= 0 and p2 >= 0:
            if s_players[p1] <= s_trainers[p2]:
                ans += 1
                p2 -= 1
                p1 -= 1
            else:
                p1 -= 1
        
        return ans
        