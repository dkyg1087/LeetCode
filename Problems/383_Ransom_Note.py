from collections import Counter as Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # If ransome note is longer than the magazine -> no way it can be contructed with it.

        if len(magazine) < len(ransomNote):
            return False
        
        # Create counters that counts the letter in both of the strings

        c1,c2 = Counter(magazine),Counter(ransomNote)

        # If ransomNote is created with the magazine, c2 should be included in c1

        return True if c1 >= c2 else False
    