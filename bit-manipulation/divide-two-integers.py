class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Edge Case: Overflow scenario
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of the quotient
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        # Subtract powers of 2 multiples of the divisor
        while a >= b:
            temp = b
            multiple = 1
            # Find the largest multiple (temp * 2^k) that fits in 'a'
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
                
            a -= temp
            quotient += multiple
            
        # Apply sign
        if negative:
            quotient = -quotient
            
        # Ensure result stays within 32-bit signed integer limits
        return max(INT_MIN, min(INT_MAX, quotient))