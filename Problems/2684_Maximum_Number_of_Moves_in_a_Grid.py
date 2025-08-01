class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        global_max = -1

        row = len(grid)
        col = len(grid[0])

        def is_legal(p_i,p_j,c_i,c_j):
            if not ((0 <= p_i < row) and (0 <= p_j < col)):
                return False
            
            if grid[p_i][p_j] < grid[i][j]:
                return True
            else:
                return False
        
        dp = [[0]*col for _ in range(row)]

        for i in range(row):
            dp[i][0] = 1

        directions = ((1,-1),(0,-1),(-1,-1))
        
        for j in range(1,col):
            for i in range(row):
                temp = []
                for delta_i,delta_j in directions:
                    if is_legal(i+delta_i,j+delta_j,i,j):
                        temp.append(dp[i+delta_i][j+delta_j])
                
                if len(temp) == 0 or max(temp) == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(temp) + 1
                
                global_max = max(global_max,dp[i][j])

        return global_max -1 if global_max != 0 else 0
                
            
            