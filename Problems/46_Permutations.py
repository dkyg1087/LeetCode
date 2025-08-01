class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Create a mask to log what elements have been used
        # after digging deep into it, we back track what we have appended and restore the state to reuse the allocated memory
        
        output = []
        mask = [True] * len(nums)

        def backtrack(output,mask,nums,cur):
            if len(cur) == len(nums):
                output.append(cur[:])
                return
            
            for i in range(len(nums)):
                if mask[i]:
                    mask[i] = False
                    cur.append(nums[i])
                    backtrack(output,mask,nums,cur)
                    cur.pop()
                    mask[i] = True
        
        backtrack(output,mask,nums,[])
        return output
