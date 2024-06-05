class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # We sum all the bit in one position in nums and mod3
        # if its not 0 then we know that the only single number has a 1 in that but position.
        # Iterate through the full 32 bit and we can compose the full 32 bit.
        

        res = 0
        
        for i in range(32):
            ct = 0
            for num in nums:
                ct += (num>>i) & 1
            
            res |= (ct%3)<<i
        
        # If the bit start with 1 it means its a negative number

        return res - 2**32 if res >> 31 & 1 else res  
                

        