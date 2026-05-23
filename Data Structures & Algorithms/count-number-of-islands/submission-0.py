class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return 0
            
            if (r,c) in seen:
                return 0
            seen.add((r,c))

            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                dfs(dr+r, dc+c)


        count = 0
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row,col) not in seen:
                    dfs(row, col)
                    count += 1

        return count

        