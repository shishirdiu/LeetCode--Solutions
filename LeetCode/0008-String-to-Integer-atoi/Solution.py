class Solution:
    def myAtoi(self, s):
        
        s = s.strip()
        if not s:
            return 0
        
        
        sign = 1
        i = 0
        
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        
        
        res = res * sign
        
        
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
