class Solution:
    def numTilings(self, n: int) -> int:

        if n < 3:
            return max(n,1)
        
        

        dp = [0] * (n + 1)

        dp[0],dp[1],dp[2] = 1,1,2

        if n < 3:
            return dp[n]

        prefix_sum = dp[0] * 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + prefix_sum
            prefix_sum += 2 * dp[i-2]
        
        return dp[-1] % (10 ** 9+7)

        
            