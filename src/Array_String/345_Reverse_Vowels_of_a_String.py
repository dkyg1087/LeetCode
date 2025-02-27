class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ""
        for c in s:
            if c in ("a","e","i","o","u","A","E","I","O","U"):
                vowels += c
        
        ans = ""

        idx = len(vowels)-1

        for c in s:
            if c in ("a","e","i","o","u","A","E","I","O","U"):
                ans += vowels[idx]
                idx -= 1
            else:
                ans += c
        
        return ans