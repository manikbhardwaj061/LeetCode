class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge cases: 1 row or string shorter than number of rows
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of string buckets for each row
        rows = [""] * numRows
        curr_row = 0
        direction = -1  # Will flip to +1 on first step
        
        for char in s:
            rows[curr_row] += char
            
            # Change direction when hitting top or bottom row
            if curr_row == 0 or curr_row == numRows - 1:
                direction = -direction
                
            curr_row += direction
            
        # Join all row strings line by line
        return "".join(rows)


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
    
    # Example 2
    print(sol.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
    
    # Example 3
    print(sol.convert("A", 1))               # Output: "A"