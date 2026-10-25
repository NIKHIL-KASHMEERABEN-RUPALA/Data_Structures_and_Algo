class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r: int, c: int) -> None:
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != 0:
                return
            grid[r][c] = 1
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in (0, cols - 1):
                if grid[r][c] == 0:
                    dfs(r, c)

        for c in range(cols):
            for r in (0, rows - 1):
                if grid[r][c] == 0:
                    dfs(r, c)

        closed_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed_count += 1
                    dfs(r, c)

        return closed_count