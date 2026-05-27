from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        INF = 2147483647
        seen = set()
        queue = deque()

        # add valid next cell to queue
        def addCell(r,c):
            if r < 0 or c < 0 or r >= ROWS or c>=COLS:
                return
            
            if (r,c) in seen or grid[r][c] == -1:
                return
            
            seen.add((r,c))
            queue.append((r,c))
        
        # add starting points for BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    seen.add((r,c))
                    queue.append((r,c))

        # process DeQueue
        dist = 0
        while queue:
            for idx in range(len(queue)):
                row,col = queue.popleft()
                if grid[row][col] == INF: grid[row][col] = dist
                
                for dr,dc in directions:
                    addCell(dr+row, dc+col)
            dist += 1
            




