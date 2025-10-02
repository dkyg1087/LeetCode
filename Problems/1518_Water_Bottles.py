class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        drinked = numBottles
        left = numBottles

        while left >= numExchange:
            K = left // numExchange
            drinked += K
            left = left - K * numExchange + K
            
        return drinked