class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        if len(word) < 5+k:
            return 0
        
        def atLeastk(word,k):
            
            window = {'a':0,'e':0,'i':0,'o':0,'u':0,'cons':0}

            wl,wr = 0,0
            ans = 0
            def isValid(k):
                nonlocal window
                for key in window.keys():
                    if key == "cons":
                        if window["cons"] < k:
                            return False
                    else:
                        if window[key] == 0:
                            return False
                
                return True
            
            while wr < len(word):
                if word[wr] in 'aeiou':
                    window[word[wr]] += 1
                else:
                    window["cons"] += 1
                
                while isValid(k):
                    ans += len(word) - wr
                    if word[wl] in 'aeiou':
                        window[word[wl]] -= 1
                    else:
                        window["cons"] -= 1
                    
                    wl += 1
                
                wr += 1
            
            return ans

        return atLeastk(word,k) - atLeastk(word,k+1)
        