class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Iterate through the list
        
        current = - 10**5
        
        current_max = current
        
        for num in nums:

            # For every element we encounter, we make a choice whether to start from this element or keep this element in the subarray.
            # If just starting from the current element is better (better than continuing the array from before) we make that the current
            # Save the max seen in current_max
            current = max(current + num, num)
            current_max = max(current_max,current)

        return current_max

