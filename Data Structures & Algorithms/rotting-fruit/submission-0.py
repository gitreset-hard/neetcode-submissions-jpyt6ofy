from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        seen = set()
        q = deque()

        def make_rotten(r,c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= ROWS or c>= COLS:
                return 
            if (r,c) in seen or grid[r][c] == 0:
                return
            
            # only fresh fruits remain , add to queue for it to become rotten
            seen.add((r,c))
            q.append((r,c))
            fresh -= 1
            grid[r][c] = 2
        
        fresh = 0
        # find all rotten fruit (2)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1


        minutes = 0
        while q and fresh > 0:
            for idx in range(len(q)):
                row,col = q.popleft()

                for dr,dc in directions:
                    nr, nc = row+dr, col + dc
                    make_rotten(nr,nc)
                    
            minutes += 1
        
        return minutes if fresh == 0 else -1


        
        