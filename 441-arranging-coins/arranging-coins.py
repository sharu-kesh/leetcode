class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        def natsum(mid):
            return (mid * (mid + 1)) // 2
        
        l = 1
        r = n
        res = 0
        while l <= r:
            mid = (l + r) // 2
            val = natsum(mid)
            if val > n:
                r = mid - 1
            else:
                res = max(res, mid)
                l = mid + 1
        return res
        