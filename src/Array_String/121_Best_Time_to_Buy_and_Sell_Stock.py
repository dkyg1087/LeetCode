class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # find the smallest along the way
        # calculate the max profit from past min price with the current iteration
        
        max_prof = 0
        min_price = prices[0]

        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            max_prof = max(max_prof,prices[i] - min_price)
        
        return max_prof


        
        

    