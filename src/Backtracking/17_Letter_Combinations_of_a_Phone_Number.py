class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # iterate through the possibilities with an index indicating where we are
        # pass the current constrcuted string into the next level
        # if we are at the end we append all into the output list

        output = []

        digitMap = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        def create_combi(digitMap,digits,digit_index,output,cur_str):
            if digit_index == len(digits) -1:
                output.extend([cur_str+alph for alph in digitMap[digits[digit_index]]])
                return 
            for alph in digitMap[digits[digit_index]]:
                create_combi(digitMap,digits,digit_index+1,output,cur_str+alph)
        
        if digits:
            create_combi(digitMap,digits,0,output,"")
        return output