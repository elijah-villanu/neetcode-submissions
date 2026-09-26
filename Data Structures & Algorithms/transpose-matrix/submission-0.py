class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # initialized with 0, size COLS x ROW instead
        res = [[0] * ROWS for x in range(COLS)]
        
        for y, row in enumerate(matrix):
            for x, i in enumerate(row):
                # new matrix will be (y, x)
                res[x][y] = matrix[y][x]
        return res