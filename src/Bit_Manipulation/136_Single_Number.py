class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # xor is interchangable, if there is only one elemnt that only appears once we can know which element it is.
        # Consider 1 xor 2 xor 3 xor 2 xor 1 xor = (1 xor 1) xor (2 xor 2) xor 3 = (0) xor (0) xor 3 = 3

        res = 0

        for num in nums:
            res ^= num

        return res 