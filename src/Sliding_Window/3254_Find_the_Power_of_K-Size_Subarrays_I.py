class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []

        if k == 1:
            return nums

        left, right = 0, 0

        while left <= len(nums) - k and right < len(nums):
            if right - left + 1 < k:
                if right < len(nums) - 1 and nums[right] != nums[right+1] -1:
                    if left == len(nums) - k:
                        res.append(-1)
                        break
                    for _ in range(left-1,min(right,len(nums) - k)):
                        res.append(-1)
                    left = right + 1
                right += 1
            else:
                res.append(nums[right])
                left += 1

        
        return res
            

