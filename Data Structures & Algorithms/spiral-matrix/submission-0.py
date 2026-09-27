class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # ring described as: rows left, columns left
        # current position
        # direction

        # each step walk in current direction and append
        # shrink (PATTERN OF SUB-PROBLEMS) and rotate direction
        # remaining unvisited area is sub rectangle set on new direction

        res = []

        def traverse(row, col, r, c, dr, dc):
            # base case, no where to go, recall this is remaining to be processed
            if row == 0 or col == 0:
                return

            for _ in range(col):
                # Step to next direction
                r += dr
                c += dc

                # Add new step
                res.append(matrix[r][c])

            # Recurse per sub rectangle, not every step like dfs
            # change direction (rows and cols size flips) inverse direction
            traverse(col, row - 1, r, c, dc, -dr)
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        traverse(ROWS, COLS, 0, -1, 0, 1)

        return res
            