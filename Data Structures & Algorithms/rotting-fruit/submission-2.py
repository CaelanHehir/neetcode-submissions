class Solution:
    def check_adjacents(self, grid: List[List[int]], target: Tuple[int]) -> bool:
        target_row = target[0]
        target_col = target[1]

        if grid[target_row][target_col] != 1:
            return False

        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                if (row_offset != 0 and col_offset != 0):
                    continue
                current_row = target_row + row_offset
                current_col = target_col + col_offset
                if not 0 <= current_row < len(grid):
                    continue
                if not 0 <= current_col < len(grid[0]):
                    continue
                if grid[current_row][current_col] == 2:
                    return True
        return False


    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        while True:
            rotting = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if self.check_adjacents(grid, (i, j)):
                        rotting.append((i, j))
            if not rotting:
                if 1 in [elem for lst in grid for elem in lst]:
                    return -1
                else:
                    return minutes
            for i, j in rotting:
                grid[i][j] = 2
            minutes += 1
        