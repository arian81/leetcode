class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        seen = set()

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        
        distance = 0
        while q:
            for n in range(len(q)):
                i, j = q.popleft()
                print(i, j)
                for di, dj in directions:
                    new_i, new_j = i + di, j + dj
                    if min(new_i, new_j) < 0 or new_i == len(mat) or new_j == len(mat[i]) or (new_i,new_j) in seen:
                        continue
                    
                    seen.add((new_i, new_j))
                    mat[new_i][new_j] = distance + 1
                    q.append((new_i, new_j))
            distance += 1

        return mat 
        