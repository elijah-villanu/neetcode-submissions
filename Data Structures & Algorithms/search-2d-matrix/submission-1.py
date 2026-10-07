class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Intuition: matrix traversal but can bypass rows due to condition (row is greater than last)

        # first traverse the first column until you find value greater than target
        # then traverse the previous row until target (or last row if no value greater found)

        last_r = -1
        for i, r in enumerate(matrix):
            if r[0] > target:
                break
            last_r = i

        if target in matrix[last_r]:
            return True
        return False