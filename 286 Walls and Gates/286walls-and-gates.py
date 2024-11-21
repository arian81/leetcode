class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        treasures = []
        len_row = len(grid)
        len_col = len(grid[0])
        q = deque()
        seen =set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        distance = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if min(nr, nc) < 0 or nr == len_row or nc == len_col or (nr, nc) in seen or grid[nr][nc] != 2147483647:
                        continue
                    
                    grid[nr][nc] = distance
                    q.append((nr, nc))
            distance +=1  

                    
