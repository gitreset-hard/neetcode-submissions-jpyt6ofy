class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == '0':
                return False
            
            if (r,c) in seen: return
            seen.add((r,c))

            for dr,dc in directions:
                nr,nc = dr+r, dc+c
                dfs(nr,nc)
                
        count = 0
        seen = set()
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) not in seen and grid[row][col] == '1':
                    dfs(row,col)
                    count += 1
        
        return count

