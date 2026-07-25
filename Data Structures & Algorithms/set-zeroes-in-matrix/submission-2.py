class Solution:
    def apply_zeroes(self, matrix: List[List[int]], target: Tuple[int]) -> None:
        target_row = target[0]
        target_col = target[1]

        # Set row to zero
        for col in range(len(matrix[target_row])):
            matrix[target_row][col] = 0

        # Set column to zero
        for row in range(len(matrix)):
            matrix[row][target_col] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        targets = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    targets.append((i, j))

        for target in targets:
            self.apply_zeroes(matrix, target)
