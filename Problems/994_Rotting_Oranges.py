class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh_cnt = 0
        fresh_dict = {}
        que = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_dict[(i,j)] = True
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    que.append((i,j))

        while len(que) != 0 and fresh_cnt > 0:
            time += 1
            for _ in range(len(que)):
                cur_i,cur_j = que.popleft()
                for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    if (cur_i+di,cur_j+dj) in fresh_dict and fresh_dict[(cur_i+di,cur_j+dj)]:
                        que.append((cur_i+di,cur_j+dj))
                        fresh_dict[(cur_i+di,cur_j+dj)] = False
                        fresh_cnt -= 1
                    
            

        return time if fresh_cnt == 0 else -1