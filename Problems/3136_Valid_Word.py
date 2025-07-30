class Solution:
    def isValid(self, word: str) -> bool:
        
        hasvowel, hasconso = False,False
        
        if len(word) < 3:
            return False
        
        for w in word:
            if w not in ascii_letters + "0123456789":
                return False
            if w in "aeiouAEIOU":
                hasvowel = True
            elif w not in "0123456789":
                hasconso  = True
        
        return hasvowel and hasconso
            
                
                
                