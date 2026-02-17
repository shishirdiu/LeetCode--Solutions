class Solution:
    def reverse(self, x):
        
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        
        res = 0
        while x != 0:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
        
        res *= sign
        
        
        if res < MIN_INT or res > MAX_INT:
            return 0
            
        return res   
