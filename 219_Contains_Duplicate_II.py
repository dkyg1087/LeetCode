class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Iterate through the list and store the seen elements in the dictionary.
        
        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:

                # If the same elements apeared before than check if it was seen less than k steps

                if abs(d[nums[i]]-i) <= k:
                    return True
                else:

                    # If the same elements was last seen more than k steps, refresh it with the new position. 

                    d[nums[i]] = i

        # If none can be found after the whole list return false.
        
        return False
        