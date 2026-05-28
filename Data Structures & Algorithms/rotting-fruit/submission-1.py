from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS , COLS = len(grid), len(grid[0])
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        seen = set()
        minutes = 0
        q = deque()
        fresh = 0
        
        def make_rotten(r,c):
            nonlocal fresh
            if r<0 or c<0 or r>= ROWS or c>=COLS or grid[r][c] == 0:
                return
            
            if grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r,c))
                fresh -= 1

        #find rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # trigger bfs from fruit
        while q and fresh > 0:
            for idx in range(len(q)): # per minute, each rotten fruit expands once
                row, col = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr+row, dc+col
                    make_rotten(nr,nc)
                    
            minutes += 1

        return minutes if fresh == 0 else -1
