class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        height_max = 0

        for g in gain:
            height += g
            height_max = max(height,height_max)
        
        return height_max
            