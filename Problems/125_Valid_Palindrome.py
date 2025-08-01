class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Run two pointers from start and end, if we hit any non alphanumeric character we skip it.
        
        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1

            # If at anypoint we got a different character means that this string is not a plindrone.

            elif s[start].lower() != s[end].lower():
                return False
            else:
                end -= 1
                start += 1
                
        
        return True

