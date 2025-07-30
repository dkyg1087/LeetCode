class Solution:
    def minChanges(self, s: str) -> int:
        dp = 0
        i = 0
        
        while i < len(s):
            if s[i] != s[i+1]:
                dp += 1
            i += 2
        
        return dp
            