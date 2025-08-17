class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        def check(i, j):
            if j < 0 and i >= 0:
                return False
            if i < 0 and j < 0: return True
            if i < 0 and j >= 0:
                for idx in range(j + 1):
                    if p[idx] != '*': return False
                return True
            if dp[i][j] != -1: return dp[i][j]
            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = check(i - 1, j - 1)
            elif p[j] == '*':
                dp[i][j] = check(i - 1, j) or check(i, j - 1)
            else:
                dp[i][j] = False
            return dp[i][j]
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return check(n - 1, m - 1)     