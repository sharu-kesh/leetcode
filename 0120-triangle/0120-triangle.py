class Solution:
    def minimumTotal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[-1])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(len(grid[i])):
                if i == 0 and j == 0: continue
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif j == len(grid[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
        return min(dp[-1])