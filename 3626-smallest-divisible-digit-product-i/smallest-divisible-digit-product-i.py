class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(num):
            prod = 1
            while num != 0:
                rem = num % 10
                prod *= rem
                num //= 10
            return prod
        while True:
            val = check(n)
            if val % t == 0:
                return n
            n += 1
