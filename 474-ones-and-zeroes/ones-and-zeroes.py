class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        dp = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(k + 1)]
        def f(idx, m, n):
            if m < 0 or n < 0:
                return 0
            if idx == k:
                return 0
            if dp[idx][m][n] != -1: return dp[idx][m][n]
            zero_count = strs[idx].count('0')
            one_count = len(strs[idx]) - zero_count

            if zero_count > m or one_count > n:
                pick = 0
            else:
                pick = 1 + f(idx + 1, m - zero_count, n - one_count)
            notpick = 0 + f(idx + 1, m, n)
            dp[idx][m][n] = max(pick, notpick)
            return dp[idx][m][n]

        return f(0, m, n)

            