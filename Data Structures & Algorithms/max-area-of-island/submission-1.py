class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        seen = set()
        max_area = 0
        area = 0

        def dfs(r,c):
            if r<0 or c<0 or r>= ROWS or c>=COLS or (r,c) in seen or grid[r][c]==0:
                return 0
            
            seen.add((r,c))
            current_area = 1
            for dr,dc in directions:
                current_area += dfs(dr+r, dc+c)
            
            return current_area
            


        area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) not in seen and grid[row][col] != 0:
                    area = dfs(row,col)
                    max_area = max(max_area, area)
        
        return max_area