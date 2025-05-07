class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        room_heap = [(0,0,0)]
        m, n = len(moveTime), len(moveTime[0])
        cost = [[math.inf] * n for _ in range(m)]
        cost[0][0] = 0

        while len(room_heap) > 0:
            c, i, j = heapq.heappop(room_heap)
            if c > cost[i][j]:
                continue
            if i == m-1 and j == n-1:
                return c
            
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ii = i + di
                jj = j + dj

                if 0 <= ii < m and 0 <= jj < n:
                    time_cost = max(c + 1, moveTime[ii][jj] + 1)
                    if time_cost < cost[ii][jj]:
                        cost[ii][jj] = time_cost
                        heapq.heappush(room_heap,(time_cost,ii,jj))
            
        return -1