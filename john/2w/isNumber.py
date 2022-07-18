class Solution:
    def isNumber(self, S: str) -> bool:    
        exp, digit, sign, dot = False, False, False, False
        for c in S:
            if c >= '0' and c <= '9': 
                digit = True     
            elif c == 'e' or c == 'E':
                if exp or not digit: 
                    return False
                else: 
                    exp, digit, sign, dot = True, False, False, False
            elif c == '+' or c == '-':
                if sign or digit or dot: 
                    return False
                else: 
                    sign = True
            elif c == '.':
                if dot or exp: 
                    return False
                else: 
                    dot = True
            else: 
                return False
        return digit
