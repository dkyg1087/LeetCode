class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}

        result = n

        
        # Brute force, store the past in dictionary to check if it is in a cycle.
        
        while True:
            
            temp = 0
            
            for c in str(result):
                temp += int(c) ** 2

            if temp == 1:
                return True
            elif temp in seen:
                return False
            else:
                seen[temp] = 1
            result = temp
            