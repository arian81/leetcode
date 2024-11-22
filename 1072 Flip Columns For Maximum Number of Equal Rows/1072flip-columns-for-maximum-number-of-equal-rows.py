class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        col_len = len(matrix[0])
        max_rows = 0

        for i in matrix:
            flipped = [not x for x in i]

            curr_max = 0
            for j in matrix:
                if j == flipped or j == i:
                    curr_max += 1
            max_rows = max(max_rows, curr_max)
        return max_rows
        