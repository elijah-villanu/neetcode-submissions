class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # No copies of matrix allowed (and none returned)

        # Think in terms of rows and columns
        # First row becomes last column, second row is second to last column..
        # Last row becomes first column

        # Aspect of rows going inverse order -> reveres rows first
        # To turn the rows into a column (transpose y, x can't work because it'll overwrite values)

        n = len(matrix)

        matrix.reverse()

        # swap method as each position will only swap once if only traversing right triangle
        offset = 1
        for r in range(n):
            for c in range(r + 1, n):
                # Swaps before overwriting
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]



            