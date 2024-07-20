class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Just do the actual addition but if there is a carry over you just move the index one to the left.
        # The only edge case would be the most significant digit, in that case we just make that 0 and append a 1 to the left
        
        index = len(digits) - 1
        while True:
            if index == -1:
                digits = [1] + digits
                break
            
            if digits[index] == 9:
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                break
        
        return digits
            
            
            