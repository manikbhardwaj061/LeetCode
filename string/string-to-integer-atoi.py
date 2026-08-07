class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Strip leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        n = len(s)
        
        # Step 2: Determine signedness
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        # Step 3: Conversion - read digits
        res = 0
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # Apply sign
        res *= sign
        
        # Step 4: Rounding (32-bit signed integer range clamping)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res