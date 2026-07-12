from heapq import heappush, heappop
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = []
        for i in arr:
            heappush(nums, i)
        cnt = 0
        di = {}
        last = float('inf')
        while nums:
            val = heappop(nums)
            if val != last:
                di[val] = cnt + 1
                last = val
                cnt += 1
        res = []

        for i in arr:
            res.append(di[i])
        
        return res
                