class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix),len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0] = matrix[0][:]
        for i in range(1, n):
            for j in range(m):
                left = dp[i - 1][j - 1] if j - 1 >= 0 else float('inf')
                up = dp[i - 1][j]
                right = dp[i - 1][j + 1] if j + 1 < m else float('inf')
                dp[i][j] = matrix[i][j] + min(left, up, right)
        return min(dp[-1])