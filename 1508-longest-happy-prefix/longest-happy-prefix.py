class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        end = -1
        for i in range(n):
            if s.endswith(s[:i]):
                end = i
        if end == -1: return ''
        return s[:end]