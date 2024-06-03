class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # Checks how many 1's are in the number

        # Just find the least signigficant bit and shift to the right everytime.

        cnt = 0

        while n:
            check = n & 1
            n = n >> 1
            cnt += check
        
        return cnt