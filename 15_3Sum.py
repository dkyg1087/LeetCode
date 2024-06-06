class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # The gist is to iterate through the whole list and run two sum on all the non dupplicate number
        # For the specific two sum to work we have to sort the list
        
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if (i != 0 and nums[i] == nums[i-1]) or nums[i] > 0:
                continue
            
            # We run 2 pointers from either side of the remaining list
            # if the sum of the current numbers is larger than 0 we move the right pointer left and vice versa

            left,right = i+1,len(nums) -1

            while left < right:
                temp = nums[i] + nums[left] + nums[right]

                if temp == 0:

                    # We find the first pair, there is still posibilty that there are still pairs so we move one of them in the next possible position

                    res.append([nums[i],nums[left],nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif temp > 0:
                    right -= 1
                else:
                    left += 1
        
        return res
