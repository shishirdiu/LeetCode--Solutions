class Solution:
    def isMatch(self, s, p):
        memo = {}

        def dp(i, j):
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            
            if j == len(p):
                return i == len(s)

            
            first_match = i < len(s) and p[j] in {s[i], '.'}

           
            if j + 1 < len(p) and p[j+1] == '*':
           
                res = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                
                res = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = res
            return res

        return dp(0, 0)
