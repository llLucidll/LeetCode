class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = x * sign

        
        string = str(x)[::-1]
        num = int(string)
        
        

        
        #upper_lim = 2**31 - 1
        #lower_lim = -2**31
        if num > 2**31 -1 and sign == 1:
            return 0
        elif num * sign < -2**31 and sign == -1:
            return 0
        
        if sign == -1:
            return num * sign
        else:
            return num

        
