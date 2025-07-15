class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) < 2:
            return 0

        intervals.sort()

        p1 = 0
        p2 = 1

        ans = 0

        while p2 < len(intervals):
            if intervals[p2][0] < intervals[p1][1]:
                ans += 1

                if intervals[p2][1] < intervals[p1][1]:
                    p1 = p2
            else:
                p1 = p2
            
            p2 += 1
            

        return ans

        