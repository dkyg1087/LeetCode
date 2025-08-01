class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Each elemenmt in profit means the best you can get so far with the amount of elements it has looked through
        # Everytime you add one element, either you exclude the last one and include this one or you exclude this one and continue.
        # it doesn't matter if the last one is actually in the optimal solution, if we actually skip this we still get the optimal.

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        
        profit = [0]*len(nums)
        

        profit[0],profit[1] = nums[0],max(nums[0],nums[1])

        for i in range(2,len(nums)):
            profit[i] = max(profit[i-2]+nums[i],profit[i-1])
        
        return profit[-1]
            


        