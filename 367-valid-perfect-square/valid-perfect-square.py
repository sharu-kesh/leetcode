class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        l = 1
        r = num // 2

        while l <= r:
            mid = (l + r) // 2
            val = mid * mid
            if val == num:
                return True
            elif val > num:
                r = mid-1
            else:
                l = mid + 1
        return False