class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        wr = 0
        vowel_count = 0
        max_count = 0

        while wr < len(s):
            if s[wr] in 'aeiou':
                vowel_count += 1
            max_count = max(max_count,vowel_count)

            if wr + 1 - k >= 0:
                if s[wr + 1 - k] in 'aeiou':
                    vowel_count -= 1
        
            wr += 1
        
        return max_count