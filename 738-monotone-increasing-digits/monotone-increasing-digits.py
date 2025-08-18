class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        ones = 111111111
        res = 0
        for i in range(9):
            while ones + res > n:
                ones //= 10
            res += ones
        return res