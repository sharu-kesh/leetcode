class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def f(i, j1, j2):
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')
            if dp[i][j1][j2] != -1: return dp[i][j1][j2]
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]
            maxi = 0
            for row in range(-1, 2, 1):
                for col in range(-1, 2, 1):
                    if j1 == j2:
                        maxi = max(maxi, grid[i][j1] + f(i + 1, j1 + row,j2 +col))
                    else:
                        maxi = max(maxi, grid[i][j1] + grid[i][j2] + f(i + 1, row + j1, j2 + col))
            dp[i][j1][j2] = maxi
            return dp[i][j1][j2]
        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        return f(0, 0, m - 1)
        