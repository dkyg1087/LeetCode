#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        isLead = True
        isPositive = True
        number = 0
        for char  in s:
            if char == " " and isLead:
                continue
            elif char in "-+" and isLead:
                if char == "-":
                    isPositive = False
                isLead = False
            elif char in "0123456789":
                number = (number*10 + int(char))
                isLead = False                
            elif isLead:
                break
            else:
                break
            # result checking
            if isPositive:
                if number > (2**31)-1 :
                    number = 2**31 - 1
                    break
            else:
                if number > (2**31):
                    number = 2**31
                    break
        if not isPositive:
            number = -number
        return number
# @lc code=end

