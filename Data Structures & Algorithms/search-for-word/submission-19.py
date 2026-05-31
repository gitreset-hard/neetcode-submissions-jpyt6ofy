class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1,0), (1,0), (0,1),(0,-1)]
        seen = set()

        def dfs(r,c, idx):
            if idx == len(word) - 1:
                return True
            
            seen.add((r,c))
            for dr, dc in directions:
                nr,nc = dr+r, dc+c
                if 0 <= nr < ROWS and  0 <= nc < COLS and (nr,nc) not in seen and board[nr][nc] == word[idx+1]:
                    if dfs(nr,nc, idx + 1):
                        return True
            seen.remove((r,c))
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row,col, 0):
                        return True
        return False