class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # same as other unique paths, just set value at obstacles to 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        dp = [0] * cols
        dp[-1] = 1

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1 , -1):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j < cols - 1:
                    dp[j] += dp[j+1]
        return dp[0]

        