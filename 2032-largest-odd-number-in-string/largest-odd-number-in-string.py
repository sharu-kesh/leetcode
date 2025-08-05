class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for r in range(n - 1, -1, -1):
            if int(num[r]) & 1:
                return num[: r + 1]
        return ''
        