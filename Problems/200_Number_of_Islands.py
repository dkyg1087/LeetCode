class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = [[True] * len(grid[0]) for _ in range(len(grid))]

        def traverse_land(grid,i,j,grid_copy):
            if grid[i][j] == "1" and grid_copy[i][j]:
                grid_copy[i][j] = False
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dir_i,dir_j in directions:
                    if 0 <= i+dir_i < len(grid) and 0 <= j+dir_j < len(grid[0]):
                        traverse_land(grid,i+dir_i,j+dir_j,grid_copy)
            return 
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and grid_copy[i][j]:
                    cnt += 1
                    traverse_land(grid,i,j,grid_copy)
        
        return cnt
