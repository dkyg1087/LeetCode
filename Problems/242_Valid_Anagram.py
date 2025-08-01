from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If the length doesn't match it can't be an anagram.
        
        if len(s) != len(t):
            return False
        
        # Create a counter for both of the strings and compare the amount of alphabets in the string.

        c1,c2 = Counter(s),Counter(t)

        # If counters are the same its an anagram.

        return True if c1 == c2 else False