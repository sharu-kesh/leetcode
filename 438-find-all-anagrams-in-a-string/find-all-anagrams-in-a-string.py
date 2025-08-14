class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m: return []
        mpp = Counter(p)
        mpp1 = Counter(s[:m])
        res = []
        # for i in range(n - m + 1):
        #     temp = Counter(s[i : i + m])
        #     if temp == mpp:
        #         res.append(i)
        # return res
        if mpp == mpp1: res.append(0)

        for i in range(m, n):
            mpp1[s[i - m]] -= 1
            mpp1[s[i]] += 1
            if mpp == mpp1: res.append(i - m + 1)
        return res
        