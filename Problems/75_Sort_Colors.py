class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0,0,0]

        for num in nums:
            cnt[num] += 1
        
        ind = 0

        for i in range(len(nums)):
            if cnt[ind] == 0:
                ind += 1
            if cnt[ind] == 0:
                ind += 1
            
            nums[i] = ind
            cnt[ind] -= 1

        return    
