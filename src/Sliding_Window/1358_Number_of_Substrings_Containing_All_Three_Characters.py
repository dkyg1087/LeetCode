class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        wl,wr = 0,0
        window = {'a':0,'b':0,'c':0}
        ans = 0

        def isValid():
            nonlocal window
            for v in window.values():
                if v == 0:
                    return False

            return True
                       
        while wr < len(s):
            
            window[s[wr]] += 1
            
            while isValid():
                ans += len(s) - wr
                window[s[wl]] -= 1
                wl += 1
                
            wr += 1
        return ans