class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        res = s
        n = len(s)
        for i in range(1, n):
            temp = s[i:] + s[:i]
            res = min(res, temp)
        return res