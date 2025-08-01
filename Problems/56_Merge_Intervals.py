class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # We sort the list by the first element of each sub list.
        # iterate through the list and merge two lists if the two lists intercepts.  

        res = sorted(intervals,key= lambda x:x[0])

        i = 0
        j = 1

        while j < len(res):
            if res[i][1] >= res[j][0]:
                temp = [res[i][0],max(res[j][1],res[i][1])]
                res.pop(i)
                res.pop(i)
                res.insert(i,temp)
            else:
                i += 1
                j += 1
        
        return res
        


        
        