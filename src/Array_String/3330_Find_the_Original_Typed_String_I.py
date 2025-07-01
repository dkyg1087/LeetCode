class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        ans =  1
        last = None
        for c in word:
            if last == c:
                ans += 1
            else:
                last = c
        
        return ans
            