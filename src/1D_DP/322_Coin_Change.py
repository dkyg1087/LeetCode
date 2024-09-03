class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp list means the best amount for the current amount
        # increase the amount each iteration
        # each iteration check if you can make a better exchange with the coin
        
        dp = [math.inf] * (amount+1)

        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        print(dp)
        return dp[-1] if dp[-1] != math.inf else -1
        
