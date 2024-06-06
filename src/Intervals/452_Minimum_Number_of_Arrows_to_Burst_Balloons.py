class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # This problem comes down to finding intersections of all the intervals
        # We sort the interval by there second element.
        # if our arrow misses, we will arange the arrow to match the furthest the arrow can be and still hit the current interval.
        
        points.sort(key= lambda x:x[1])

        cnt = 0
        a_pos = -2e10


        for point in points:

            if point[1] >= a_pos >= point[0]:
                continue
            else:
                cnt += 1
                a_pos = point[1]
        
        return cnt
            


