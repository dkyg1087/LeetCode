class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # dp to add possiblilties to the next square
        
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j+1 < len(dp[0]) and obstacleGrid[i][j+1] == 0:
                    dp[i][j+1] += dp[i][j]
                if i+1 < len(dp) and obstacleGrid[i+1][j] == 0:
                    dp[i+1][j] += dp[i][j]
            
        return dp[-1][-1]
                    
                     