class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res  = []
        board = [["." for _ in range(n)] for _ in range(n)]

        pos_diag = set()
        neg_diag = set()
        col_used = set()
        """
            pos_diag
            0 1 2 3
            1 2 3 4
            2 3 4 5
            3 4 5 6
        """
        def backtrack(row):

            # base case, got to final row -> valid
            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return

            # solve 1 row at a time
            for col in range(n):
                if (
                    col in col_used 
                    or (row+col) in pos_diag 
                    or (row-col) in neg_diag
                ):
                    continue
                
                # add a Queen
                col_used.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)
                board[row][col] = "Q"

                backtrack(row+1)

                # remove Queen
                col_used.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)
                board[row][col] = "."
        
        backtrack(0)
        return res
                    