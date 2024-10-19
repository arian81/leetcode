# import numpy as np

class Solution:
    def rotate(self, array: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #first we transpose
        for row in range(len(array)):
            for col in range(row + 1, len(array[row])):
                array[row][col], array[col][row] = array[col][row], array[row][col]

        for row in range(len(array)):
            for col in range(len(array[row]) // 2):
                array[row][col], array[row][len(array[row]) - col - 1] = array[row][len(array[row]) - col - 1], array[row][col]

        