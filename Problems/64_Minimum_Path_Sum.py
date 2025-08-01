class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # dp to run through the whole possibility with 2D dp
        # can be optimized to only use 1D instead of 2D
        # but I'm a bit lazy
        
        dp = [[math.inf]*len(grid[0]) for _ in range(len(grid))]

        dp[0][0] = grid[0][0]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j+1 < len(dp[0]):
                    dp[i][j+1] = min(dp[i][j+1],dp[i][j] + grid[i][j+1])
                if i+1 < len(dp):
                    dp[i+1][j] = min(dp[i+1][j],dp[i][j] + grid[i+1][j])
        
        return dp[-1][-1]

        