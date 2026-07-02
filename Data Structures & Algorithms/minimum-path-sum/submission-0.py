class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        dp[0][0] = grid[0][0]

        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) == (0,0):
                    continue

                if row == 0:
                    dp[row][col] = dp[row][col-1] + grid[row][col]
                
                elif col == 0:
                    dp[row][col] = dp[row-1][col] + grid[row][col]

                else:
                    left = dp[row][col-1]
                    top = dp[row-1][col]
                    dp[row][col] = grid[row][col] + min(left,top)

        return dp[ROWS-1][COLS-1]
