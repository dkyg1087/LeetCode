class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1,len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]
        
        for i in range(len(nums)):
            if i == 0:
                if prefix_sum[-1] - prefix_sum[i] == 0:
                    return i 
            elif i == len(nums)-1:
                if prefix_sum[-1] - nums[i] == 0:
                    return i
            else:
                if prefix_sum[i-1] == prefix_sum[-1] - prefix_sum[i]:
                    return i
        
        return -1
            
        
        
            