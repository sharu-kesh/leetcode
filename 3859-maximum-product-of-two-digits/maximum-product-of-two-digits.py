class Solution:
    def maxProduct(self, n: int) -> int:
        max1, max2 = -1, -1
        while n:
            rem = n % 10
            if rem >= max1 and max1 >= max2:
                max2 = max1
                max1 = rem
            elif rem >= max2:
                max2 = rem
            n //= 10
        return max1 * max2