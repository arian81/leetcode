class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = []
        row_len = len(grid)
        col_len = len(grid[0])
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh.append((i,j))
        if len(fresh) == 0:
            return 0
        q = deque(rotten)
        
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        while q:
            print(minutes, q)
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            
            minutes += 1

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    return -1
        return minutes - 1
            
                        
            



        