class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Spiral but reveresed

        res = [[0] * n for _ in range(n)]
        total = n * n

        def build(row, col, r, c, dr, dc, val):
            if row == 0 or col == 0:
                return
            
            for _ in range(col):
                r += dr
                c += dc
                res[r][c] = val
                val += 1

            # change direction
            build(col, row - 1, r, c, dc, -dr, val)


        build(n, n, 0, -1, 0, 1, 1)
        
        return res