class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 : return False
        val = ceil(log(n, 3))
        return pow(3, val) == n