class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        mpp1 = Counter(p)
        if n == m:
            return [0] if Counter(s) == mpp1 else []
        r = m - 1
        l = 0
        res = []
        while r < n:
            if Counter(s[l : r + 1]) == mpp1:
                res.append(l)
            l += 1
            r += 1
        return res
        