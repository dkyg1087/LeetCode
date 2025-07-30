class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seen = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                seen += 1
            else:
                nums[i-seen] = nums[i]
                if seen != 0:
                    nums[i] = 0
        
        return