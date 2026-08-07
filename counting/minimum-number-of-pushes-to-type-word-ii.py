from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each letter
        freq = Counter(word)
        
        # Sort frequencies in descending order
        sorted_freqs = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(sorted_freqs):
            # Calculate push multiplier (1st 8 letters get 1, 2nd 8 get 2, etc.)
            pushes_per_char = (i // 8) + 1
            total_pushes += count * pushes_per_char
            
        return total_pushes