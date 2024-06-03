class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        # This comes down to finding the common bitwise prefix of left and right
        # We minus 1 from right to eliminate the right most 1 in the bit wise representation.
        # find do it until it is less than left 
        
        while left < right:
            right &= (right-1)
        return right