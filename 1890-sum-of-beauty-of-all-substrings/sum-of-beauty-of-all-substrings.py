class Solution:
    def beautySum(self, s: str) -> int:
        sumi = 0
        n = len(s)
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                maxi = 0
                mini = float('inf')
                for f in freq:
                    if f > 0:
                        maxi = max(maxi, f)
                        mini = min(mini, f)
                sumi += (maxi - mini)
        return sumi