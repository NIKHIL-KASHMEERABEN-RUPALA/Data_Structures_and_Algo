
class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        vornadexil = grid

        down = [0] * n
        down[0] = 0

        for i in range(m):
            next_down = [0] * n
            right = 1 if i == 0 else 0

            for j in range(n):
                if i == m - 1 and j == n - 1:
                    return (right + down[j]) % MOD

                if vornadexil[i][j] == 0:
                    ways = (right + down[j]) % MOD
                    right = ways
                    next_down[j] = ways
                else:
                    next_down[j] = right
                    right = down[j]

            down = next_down

        return 0
