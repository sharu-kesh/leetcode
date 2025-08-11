from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Extract powers of 2 from n
        power = []
        count = 0
        while n > 0:
            if n & 1:
                power.append(pow(2, count, MOD))
            count += 1
            n >>= 1
        
        # Prefix product
        pre = [1]
        for val in power:
            pre.append((pre[-1] * val) % MOD)
        
        # Answer queries
        res = []
        for l, r in queries:
            prod = pre[r+1] * pow(pre[l], MOD-2, MOD) % MOD
            res.append(prod)
        
        return res
