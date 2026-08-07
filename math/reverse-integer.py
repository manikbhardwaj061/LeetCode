class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine sign and reverse the absolute string representation
        sign = -1 if x < 0 else 1
        res = sign * int(str(abs(x))[::-1])
        
        # Check 32-bit signed integer boundary
        return res if INT_MIN <= res <= INT_MAX else 0
        