class Solution:
    def check_row(self, board: List[List[str]], row: int) -> bool:
        filled = [val for val in board[row] if val != '.']
        uniques = set(filled)
        return len(filled) == len(uniques)

    def check_col(self, board: List[List[str]], col: int):
        column = [board[i][col] for i in range(len(board))]
        filled = [val for val in column if val != '.']
        uniques = set(filled)
        return len(filled) == len(uniques)

    def check_subgrid(self, board: List[List[str]], row_val: int, col_val: int) -> bool:
        start_row = 0 + row_val * 3
        start_col = 0 + col_val * 3

        filled = []
        for i in range(3):
            for j in range(3):
                value = board[start_row + i][start_col + j]
                if value != '.':
                    filled.append(value)

        uniques = set(filled)
        return len(filled) == len(uniques)


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in range(len(board)):
            if not self.check_row(board, row):
                return False

        # Check cols
        for col in range(len(board[0])):
            if not self.check_col(board, col):
                return False

        # Check subgrids
        for i in range(3):
            for j in range(3):
                if not self.check_subgrid(board, i, j):
                    return False

        return True
        
