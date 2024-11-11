class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_col = len(grid[0])
        len_row = len(grid)


        count = 0

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        

        def dfs(grid, start):

            r, c = start

            if min(r, c) < 0 or len_col == c or len_row == r or grid[r][c] == "0":
                return 

            grid[r][c] = "0"

            for rd, cd in directions:
                dfs(grid, (r + rd, c + cd))

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    dfs(grid, (row, col))
                    count += 1
        return count
