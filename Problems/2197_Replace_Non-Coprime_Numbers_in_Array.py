class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a
        
        def lcm(a,b):
            return a * b // gcd(a,b)
        
        if len(nums) == 1:
            return nums

        ans = [nums[0]]

        i = 1
        
        while i < len(nums):
            targ = nums[i]
            while len(ans) != 0 and gcd(ans[-1],targ) != 1:
                targ = lcm(ans[-1],targ)
                ans.pop()
            ans.append(targ)
            i += 1

                    
        return ans
            