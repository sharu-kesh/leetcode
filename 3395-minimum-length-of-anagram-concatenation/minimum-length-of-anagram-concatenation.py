class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        c = Counter(s)
        g = n//gcd(*c.values())
        for i in range(g, n//2+1, g):
            if n % i != 0:
                continue
            for j in range(i, n, i):
                if sorted(s[:i]) != sorted(s[j:j+i]):
                    break
            else:
                return i
        return n