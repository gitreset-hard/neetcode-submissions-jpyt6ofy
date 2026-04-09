class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.exists = False

        ROWS, COLS = len(board), len(board[0])
        directions = ((-1,0),(0,1),(1,0),(0,-1))
        
        def dfs(r,c, idx, vis):
            if idx == len(word):
                self.exists = True
                return 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in vis or board[r][c] != word[idx]:
                return False

            vis.add((r,c))
        
            for dr,dc in directions:
                nr,nc = dr+r, dc+c
                dfs(nr, nc, idx + 1, vis)
            
            vis.remove((r,c))
    
        for row in range(ROWS):
            for col in range(COLS):
                vis = set() # can't revisit the same cell per attempt 
                if not self.exists:
                    if board[row][col] == word[0]:
                        dfs(row,col, 0, vis)
                    
        
        return self.exists