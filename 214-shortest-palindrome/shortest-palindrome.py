class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        n = len(s)
        for i in range(n):
            if s.startswith(rev[i:]):
                return rev[:i] + s
        return s