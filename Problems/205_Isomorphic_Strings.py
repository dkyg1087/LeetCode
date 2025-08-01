class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # If the strings can map one to one, the length of the mapped set should be the same length as both the strings.

        return len(set(zip(s,t))) == len(set(s)) == len(set(t))