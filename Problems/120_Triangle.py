class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # actually run through all the possiblilty with dp
        # iterate through two list to preserve space

        dp = [triangle[0][0]]
        next_dp = []
        for i in range(1,len(triangle)):
            next_dp = [math.inf] * (len(dp) + 1)
            for j in range(len(dp)):
                next_dp[j] = min(next_dp[j],dp[j]+triangle[i][j])
                next_dp[j+1] = min(next_dp[j+1],dp[j]+triangle[i][j+1])
            print(dp,next_dp)
            dp = next_dp
        
        return min(dp)