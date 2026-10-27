class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#']*n for _ in range(m)]
        i , j = 0 , 0 

        grid[i][j] = '.'
        while j < n-1:
            grid[i][j+1] = '.'
            j+=1

        while i < m-1:
            grid[i+1][j] = '.'
            i+=1
        
        return [''.join(row) for row in grid]
