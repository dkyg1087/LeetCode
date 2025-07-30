class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # s is a subseq of t -> t >= s

        # Iterate through the longer string and found every character in the string

        if len(s) == 0:
            return True

        ptr = 0

        for i in range(len(t)):
            if t[i] == s[ptr]:
                ptr += 1
            
            if ptr == len(s):
                return True
            
        return False