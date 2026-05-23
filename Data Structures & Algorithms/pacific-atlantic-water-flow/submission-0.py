class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def dfs(r,c, seen, prev):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in seen or heights[r][c] < prev:
                return 0
            
            seen.add((r,c))
            for dr,dc in directions:
                dfs(dr+r, dc+c, seen, heights[r][c])
            
        
        pacific = set()
        atlantic = set()
        for col in range(COLS):
            # row = 0 
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS-1, col, atlantic, heights[ROWS-1][col])

        for row in range(ROWS):
            dfs(row,0, pacific, heights[row][0])
            dfs(row, COLS-1, atlantic, heights[row][COLS-1])

        result = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) in pacific and (row,col) in atlantic:
                    result.append([row,col])
        
        return result
            