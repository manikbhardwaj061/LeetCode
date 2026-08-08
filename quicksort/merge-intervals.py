from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If no overlap, append the current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap exists; extend the previous interval's end time
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged