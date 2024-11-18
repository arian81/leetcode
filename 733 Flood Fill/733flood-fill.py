class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        len_row = len(image)
        len_col = len(image[0])
        src_image_color = image[sr][sc]
        def dfs(image, curr):
            row, col = curr

            if min(row, col) < 0 or row >= len_row or col >= len_col or image[row][col] == color or image[row][col] != src_image_color:
                return

            image[row][col] = color
            
            for dr, dc in directions:
                dfs(image, (row + dr, col + dc))
        
        dfs(image, (sr, sc))
        return image
        