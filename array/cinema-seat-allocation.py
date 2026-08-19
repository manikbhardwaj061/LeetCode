from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Map each row to a bitmask representing reserved seats (only seats 2 to 9 matter)
        reserved_mask = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved_mask[row] |= (1 << seat)
        
        # Bitmasks for the three possible 4-seat blocks
        # Left block: seats 2, 3, 4, 5
        left_mask = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)     # 0b00111100 (60)
        # Right block: seats 6, 7, 8, 9
        right_mask = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)   # 0b1111000000 (960)
        # Middle block: seats 4, 5, 6, 7
        middle_mask = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)  # 0b11110000 (240)
        
        # Start by assuming all n rows can fit 2 groups each
        total_groups = (n - len(reserved_mask)) * 2
        
        # Process only the rows that have reservations in seats 2..9
        for mask in reserved_mask.values():
            left_free = (mask & left_mask) == 0
            right_free = (mask & right_mask) == 0
            middle_free = (mask & middle_mask) == 0
            
            if left_free and right_free:
                total_groups += 2
            elif left_free or right_free or middle_free:
                total_groups += 1
                
        return total_groups