class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in matrix:
            low = 0
            high = cols - 1
            while low != high:
                mid = (high + low) // 2
                if row[mid] == target:
                    return True
                if row[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            if row[low] == target:
                return True
        return False
