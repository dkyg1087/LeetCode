class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        odd_max = -1 * math.inf
        even_min = math.inf

        for key in c:
            if c[key] % 2 == 0:
                even_min = min(even_min,c[key])
            else:
                odd_max = max(odd_max,c[key])
        
        return odd_max - even_min