class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)

        maxx = -1

        for key in c.keys():
            if key == c[key]:
                maxx = max(maxx,key)

        return maxx    