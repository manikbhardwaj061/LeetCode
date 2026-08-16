class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        # Count frequencies of stones remainder modulo 3
        cnt = [0, 0, 0]
        for s in stones:
            cnt[s % 3] += 1
            
        c0, c1, c2 = cnt[0], cnt[1], cnt[2]
        
        # If the count of 0-mod stones is even, they cancel out in turn order
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        # If the count of 0-mod stones is odd, Alice wins only if |c1 - c2| > 2
        else:
            return abs(c1 - c2) > 2