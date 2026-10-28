
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MAX_XOR = 1024

        dp = [[0] * MAX_XOR for _ in range(n)]

        for i in range(m):
            for j in range(n):
                value = grid[i][j]

                if i == 0 and j == 0:
                    dp[j][value] = 1
                    continue

                prev = dp[j][:]
                dp[j] = [0] * MAX_XOR

                for x in range(MAX_XOR):
                    if prev[x]:
                        dp[j][x ^ value] = 1

                    if j > 0 and dp[j - 1][x]:
                        dp[j][x ^ value] = 1

        for x in range(MAX_XOR):
            if dp[n - 1][x]:
                return x

        return 0
