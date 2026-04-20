class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up

        grid = [[0] * (n+1) for _ in range(m+1)]
        grid[m-1][n-1] = 1
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                # edges
                # if row == m - 1  or col == n - 1:
                #     grid[row][col] = 1
                #     continue

                grid[row][col] += grid[row + 1][col] + grid[row][col + 1]
        
        return grid[0][0]