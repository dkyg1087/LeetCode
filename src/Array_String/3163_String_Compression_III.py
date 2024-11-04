class Solution:
    def compressedString(self, word: str) -> str:
        comp = []

        c_char = ""
        char_cnt = 0

        for c in word+"%":
            if c != c_char:
                if char_cnt != 0:
                    comp.append("".join([str(char_cnt),c_char]))

                c_char = c
                char_cnt = 1
            
            else:
                char_cnt += 1
                if char_cnt == 10:
                    comp.append("".join((["9",c_char])))
                    char_cnt = 1
        
        return "".join(comp)
                
                    

        