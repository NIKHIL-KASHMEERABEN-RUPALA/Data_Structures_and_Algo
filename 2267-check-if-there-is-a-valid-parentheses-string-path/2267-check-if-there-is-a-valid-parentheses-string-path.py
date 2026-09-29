class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        # A valid path length (m + n - 1) must be even (i.e., m + n must be odd),
        # must start with '(' and end with ')'
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # Initial state: balance 0 before entering (0, 0)
        
        for i in range(m):
            row = dp[i]
            prev_row = dp[i - 1] if i > 0 else None
            for j in range(n):
                if i == 0 and j == 0:
                    mask = 1
                else:
                    mask = 0
                    if i > 0:
                        mask |= prev_row[j]
                    if j > 0:
                        mask |= row[j - 1]
                
                if mask:
                    row[j] = mask << 1 if grid[i][j] == '(' else mask >> 1
                    
        return (dp[m - 1][n - 1] & 1) == 1