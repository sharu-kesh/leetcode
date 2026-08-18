from heapq import heappush, heappop
from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)
        if k == 1:
            heap = []
            for key, val in freq.items():
                heappush(heap, (-key, val))
            while heap:
                key, val = heappop(heap)
                if val == 1: return -1 * key
            return -1
        if k == n: return max(nums)
        count1 = freq[nums[0]]
        count2 = freq[nums[-1]]
        if count1 == 1 and count2 == 1: return max(nums[0], nums[-1])
        elif count1 == 1: return nums[0]
        elif count2 == 1: return nums[-1]
        return -1

        
        