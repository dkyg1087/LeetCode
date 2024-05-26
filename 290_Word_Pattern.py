class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # split s into list for easier match.

        l = s.split(" ")

        # If the length doesn't match then it won't be a full match.
        
        if len(l) != len(pattern):
            return False
        
        # Create a dictionary to store matches

        d = {}
        
        # Create a match between the two if it has not been seen before, 

        for i in range(len(l)):
            if pattern[i] not in d:
                d[pattern[i]] = l[i]
            else:

                # If it has been seen before, make sure if it's the same, if it's not the same we know this can't be a direct match.

                if d[pattern[i]] != l[i]:
                    return False
        
        # If there's no bad matches it's a full match.         

        return True
