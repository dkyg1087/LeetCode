class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Store the index and value for the elements seen before
        # Check if the elements have been seen before by looking at the difference between the target and current iteration
        
        d = {}

        for i in range(len(nums)):
            if target-nums[i] not in d:
                d[nums[i]] = i
            
            else:
                return [d[target-nums[i]],i]