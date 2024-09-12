class Solution:
    def intToRoman(self, num: int) -> str:
        
        # Greedy method, if the largest one can fit we fit then substract
        # repeate till zero.
        
        roman_dict = {
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            8:"VIII",
            7:"VII",
            6:"VI",
            5:"V",
            4:"IV",
            3:"III",
            2:"II",
            1:"I"           
        }
        res = ""
        for key in roman_dict.keys():
            if num // key > 0:
                res += (roman_dict[key] * (num // key))
                num -= key * (num//key)
        
        return res
                