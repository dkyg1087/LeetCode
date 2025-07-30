class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Every element added in this dictionary will be initialized with a length of 1.
        # We check the nearby neighbor with their max length.
        # If there are nearby neighbors we update the element itself and the most outer element.
        # We only update the most outer elemnt because only they can indicate the max length of the whole sequence when we add any new element.  
        
        d = {}
        res_max = 0

        for num in nums:
            
            # Takes care of duplicates by ignoring it if its already in the dictionary.
            
            if num not in d:

                # Check the left and right bound for existing max length

                left = 0 if num-1 not in d else d[num-1]
                right = 0 if num+1 not in d else d[num+1]
                                

                d[num] = left + right + 1

                # Update the left and right bound with the new max length with this new element added 
                
                d[num-left] = d[num+right] = d[num]

                res_max = max(d[num],res_max)

        return res_max
            
            