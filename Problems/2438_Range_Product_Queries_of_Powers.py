class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        powers = []
        cur = 1
        num = n
        po = 0
        ans = []

        while num != 0:
            if num & 1 == 1:
                powers.append(cur * (2 ** po))
                cur = powers[-1]
            po += 1
            num >>= 1

        for left,right in queries:
            if left == 0:
                ans.append(powers[right] % (10 ** 9 + 7))
            else:
                ans.append((powers[right]//powers[left-1]) % (10 ** 9 + 7))
        
        return ans
            