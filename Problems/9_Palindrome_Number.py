class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True

        digits = int(log(x,10)+1)
        num = x
        reversed_num = 0

        # odd  -> reverse until the same digits, discard the mid point
        # even -> reverse until the same digits

        if digits == 1:
            return True

        for _ in range(digits//2):
            temp = num % 10
            reversed_num = reversed_num*10 + temp
            num = num // 10
            print(num,reversed_num)
        
        if digits % 2 == 1:
            num = num // 10
        
        return True if num == reversed_num else False
