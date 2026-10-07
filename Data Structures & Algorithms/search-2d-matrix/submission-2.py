class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last_r = -1
        for i, r in enumerate(matrix):
            if r[0] > target:
                break
            last_r = i

        if target in matrix[last_r]:
            return True
        return False