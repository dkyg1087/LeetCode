class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        que = deque([tuple(entrance)])
        visited = {tuple(entrance):True}
        step = 0
        while len(que) != 0:
            step += 1
            for _ in range(len(que)):
                cur_i,cur_j = que.popleft()

                for d_i,d_j in ((-1,0),(1,0),(0,1),(0,-1)):
                    delta_i,delta_j = d_i + cur_i,d_j + cur_j

                    
                    if (delta_i,delta_j) in visited or delta_i < 0 or delta_j < 0 or delta_i == len(maze) or delta_j == len(maze[0]):
                        continue
                    if maze[delta_i][delta_j] == ".":
                        if delta_i == 0 or delta_i == len(maze) - 1 or delta_j == 0 or delta_j == len(maze[0]) - 1:
                            return step
                        else:
                            que.append((delta_i,delta_j))
                            visited[(delta_i,delta_j)] = True
                    
                    
        
        return  -1