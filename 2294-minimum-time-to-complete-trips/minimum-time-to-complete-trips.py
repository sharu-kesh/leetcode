class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 1
        r = max(time) * totalTrips

        def check(mid):
            count = 0
            for i in time:
                count += mid // i
            return count >= totalTrips

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l