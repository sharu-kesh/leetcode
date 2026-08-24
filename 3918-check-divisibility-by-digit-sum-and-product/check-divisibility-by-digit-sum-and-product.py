class Solution:
    def checkDivisibility(self, n: int) -> bool:

        def calc(val):
            sumi = 0
            prod = 1
            while val > 0:
                rem = val % 10
                sumi += rem
                prod *= rem
                val //= 10
            return [sumi, prod]
        
        sumi, prod = calc(n)
        # print(sumi, prod)
        return n % (sumi + prod) == 0
        