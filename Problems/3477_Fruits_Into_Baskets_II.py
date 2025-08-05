class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        res = 0

        for fruit in fruits:
            stored = False
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets[i] = 0
                    stored = True
                    break
            
            if not stored:
                res += 1
        

        return res

                