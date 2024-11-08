class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        res = []
        target = (2**maximumBit) - 1
        cur = 0

        for num in nums:
            cur ^= num
            res.append(target ^ cur)
            
        return res[::-1]