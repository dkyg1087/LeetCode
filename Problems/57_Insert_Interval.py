class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            start,end  = intervals[i]

            # The current interval is After newInterval

            if start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]

            # The current interval is before newInterval

            elif end < newInterval[0]:
                res.append(intervals[i])
            
            # Update newInterval with current info by combine it with current.

            else:
                newInterval = [min(newInterval[0],start),max(newInterval[1],end)]
        
        # If the for loop end means that the new Interval will append on the last.

        res.append(newInterval)

        return res
        