class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # Negative numbers are not palindromes.
        # Numbers ending in 0 (except 0 itself) are not palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # When length is odd, we drop middle digit via reverted_number // 10
        return x == reverted_number or x == reverted_number // 10
        