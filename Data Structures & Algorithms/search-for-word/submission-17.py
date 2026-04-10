class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        """
            only alphabets, not nums

            DFS or BFS

            num of islands style
        """

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in vis: 
                return False

            if board[r][c] == word[idx]:
                    
                
                vis.add((r,c)) 

                directions = [[0,-1], [-1,0],[0,1],[1,0]]
                for dr,dc in directions:
                    if dfs(r+dr, c+dc ,idx+1):
                        return True
                
                vis.remove((r,c))


        ROWS, COLS = len(board), len(board[0])
        vis = set()
        for row in range(ROWS):
            for col in range(COLS):
                # search of first char
                if dfs(row,col, 0): 
                    return True

        return False