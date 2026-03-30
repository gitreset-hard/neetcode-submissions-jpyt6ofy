class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force
        # check rows
        seen_row = defaultdict(set)
        seen_col = defaultdict(set)
        seen_sq = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                num = board[row][col]
                containers = (seen_row[row], seen_col[col], seen_sq[row//3,col//3])
                if any(num in c for c in containers):
                    return False
                seen_row[row].add(num)
                seen_col[col].add(num)
                seen_sq[row//3,col//3].add(num)
        
        return True