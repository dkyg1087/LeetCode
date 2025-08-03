class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        

        ans = []

        for spell in spells:
            #print(success/spell, bisect_left(potions,success / spell))
            ans.append(len(potions) - bisect_left(potions,success / spell))
        
        return ans