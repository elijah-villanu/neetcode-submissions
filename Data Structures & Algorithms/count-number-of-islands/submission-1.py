class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # At least one island
        count = 0
        # calculation to be done on indices to move
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        # recursive definition
        def dfs(r, c):
            # if cell is out of bounds or is 0 (base case)
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            
            # mark as visited (so it doesn't get double counted as we traverse)
            grid[r][c] = "0"

            # look (dfs) at all neighbor cells
            for dr, dc in directions:
                dfs(dr + r, dc + c)
            
        # traverse through each cell in grid
        for row in range(ROWS):
            for col in range(COLS):
                # island marked (dfs will mark adjacent nodes 0 so not double counted)
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        
        return count


