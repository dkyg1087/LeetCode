class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # Iterate through the list and store the last one to see if it is consecutive.

        start,end,last = None,None,None
        res = []
        
        if len(nums) == 0:
            return res

        for num in nums:
            if last is None:
                last = num
                start = last
            elif num - last == 1:
                last = num
            else:
                end = last

                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(end))
                
                end = None
                start = num
                last = num
        else:
            end = last
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start)+"->"+str(end))
        
        return res
                     
            

        

                

        