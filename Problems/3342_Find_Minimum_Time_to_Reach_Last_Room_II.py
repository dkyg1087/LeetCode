class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        cost_heap = [(0,0,0,0)]
        cost_map = [[math.inf] * n for _ in range(m)]

        while len(cost_heap) > 0:
            time,step,i,j = heapq.heappop(cost_heap)
            if time > cost_map[i][j]:
                continue
            if i == m-1 and j == n - 1:
                return time
            
            for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n:
                    cost = max(time,moveTime[ii][jj]) + (1 if step % 2 == 0 else 2)
                    if cost < cost_map[ii][jj]:
                        cost_map[ii][jj] = cost
                        heapq.heappush(cost_heap,(cost,step+1,ii,jj))
        
        return -1