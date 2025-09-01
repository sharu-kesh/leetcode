class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair = sorted(zip(nums1, nums2), key = lambda x : -x[1])
        minH = []
        tot = 0
        res = 0

        for i, j in pair:
            tot += i
            heappush(minH, i)

            if len(minH) > k:
                tot -= heappop(minH)
            if len(minH) == k:
                res = max(res, tot * j)
        return res