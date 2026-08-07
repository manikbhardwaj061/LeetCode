class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Transform string to avoid even/odd handling: "abc" -> "^#a#b#c#$"
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        P = [0] * n
        C = R = 0
        
        for i in range(1, n - 1):
            i_mirror = 2 * C - i
            if R > i:
                P[i] = min(R - i, P[i_mirror])
            
            # Expand around center i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            
            # Update center and right border if expanded beyond R
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        # Find maximum element in P
        max_len, center_index = max((val, idx) for idx, val in enumerate(P))
        start = (center_index - max_len) // 2
        return s[start : start + max_len]
        