class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums)+1)

        for left,right in queries:
            diff[left] += 1
            diff[right+1] -= 1
        
        for i in range(len(nums)):
            if nums[i] > diff[i]:
                return False
            else:
                diff[i+1] += diff[i]
        
        return True