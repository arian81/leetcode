class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])
        
        if grid[0][0] == 1 or grid[len_row-1][len_col-1] == 1:
            return -1

        q = deque()

        q.append((0,0))

        visited = set((0,0))
        length = 1
        
        
        directions = [
                        (1, 1),
                        (1, -1),
                        (1, 0),
                        (-1, 1),
                        (-1, -1),
                        (-1, 0),
                        (0, 1),
                        (0, -1),
                     ]

        while q:

            for i in range(len(q)):
                r , c = q.popleft()
                if r == len_row - 1 and c == len_col -1 :
                    return length
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr, nc) in visited or min(nr, nc) < 0 or nr == len_row or nc == len_col or grid[nr][nc] == 1:
                        continue
                    
                    visited.add((nr, nc))
                    q.append((nr, nc))
            length += 1
        return -1

        