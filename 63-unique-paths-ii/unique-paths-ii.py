class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1 if not grid[0][0] else 0
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0: continue
                if grid[i][j] == 1: dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # print(dp)
        return dp[-1][-1]
        