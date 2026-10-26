class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        w = n + 2
        a = [0] * ((m + 2) * w)

        for i in range(m):
            p = (i + 1) * w + 1
            a[p:p + n] = grid[i]

        ans = 0

        for i in range(1, m + 1):
            p = i * w + 1
            end = p + n

            while p < end:
                if a[p]:
                    total = a[p]
                    a[p] = 0
                    stack = [p]

                    while stack:
                        x = stack.pop()

                        y = x - w
                        if a[y]:
                            total += a[y]
                            a[y] = 0
                            stack.append(y)

                        y = x + w
                        if a[y]:
                            total += a[y]
                            a[y] = 0
                            stack.append(y)

                        y = x - 1
                        if a[y]:
                            total += a[y]
                            a[y] = 0
                            stack.append(y)

                        y = x + 1
                        if a[y]:
                            total += a[y]
                            a[y] = 0
                            stack.append(y)

                    if total % k == 0:
                        ans += 1

                p += 1

        return ans