    class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        even -> ele all odds or ele all even
        odd -> odd even odd even odd even or eve odd even odd

        True -> odd
        False -> even
        """

        cost = [0,0,0,0]
        last3,last4 = False,True
        for num in nums:
            if num % 2 == 1:
                cost[0] += 1
            else:
                cost[1] += 1
            #check for odd even
            if last3: # if the last one is odd this one needs to be even
                if num % 2 == 1:
                    cost[2] += 1
                else:
                    last3 = not last3
            else: # last one is even
                if num % 2 == 0:
                    cost[2] += 1
                else:
                    last3 = not last3
            
            # check for even odd

            if last4: #if the last one is odd this one needs to bee even
                if num % 2 == 1:
                    cost[3] += 1
                else:
                    last4 = not last4
            else:
                if num % 2 == 0:
                    cost[3] += 1
                else:
                    last4 = not last4

        return len(nums) - min(cost)

    