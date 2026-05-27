class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        seen = set()
        border_zeros = set()
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in seen or board[r][c] != "O":
                return

            seen.add((r,c))
            for dr, dc in directions:
                dfs(dr+r, dc+c)
        
        # trigger search from border only
        for r in (0,ROWS-1):
            for c in range(COLS):
                if board[r][c] == "O":
                    dfs(r,c)
        
        for r in range(ROWS):
            for c in (0, COLS-1):
                if board[r][c] == "O":
                    dfs(r,c)
            
        # find all zeroes and if they're not in border_zeros, then convert to X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in seen:
                    board[r][c] = "X"
        
