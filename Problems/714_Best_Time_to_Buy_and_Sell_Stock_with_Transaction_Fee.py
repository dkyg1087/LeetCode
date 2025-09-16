class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        hold = [0] * len(prices)
        free = [0] * len(prices)

        hold[0] = -prices[0]

        for i in range(1,len(prices)):
            hold[i] = max(hold[i-1],free[i-1] - prices[i])
            free[i] = max(free[i-1],hold[i-1] + prices[i] - fee)

        return free[-1]
