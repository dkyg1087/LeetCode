class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        # Simply count how many 5s are in that number
        # Don't forget when there is 25,125.... you have to count multiple times
        
        zero_count = 0

        while n > 0:
            n //= 5
            zero_count += n
        
        return zero_count
            