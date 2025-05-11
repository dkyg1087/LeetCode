class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        STATE = -1

        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                STATE = -1
            else:
                STATE += 1

            if STATE == 2:
                return True
        
        return False
            
            
            