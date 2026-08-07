class Solution:
    def minPartitions(self, n: str) -> int:
        # The answer is simply the maximum digit present in the string n
        return int(max(n))