class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3 = len(nums)
        n = n3 // 3
        
        left_min = [0] * n3
        right_min = [0] * n3

        max_heap = []
        left_sum = 0
        for i in range(n3):
            heappush(max_heap, -nums[i])
            left_sum += nums[i]
            if len(max_heap) > n:
                left_sum += heappop(max_heap)
            if i >= n - 1:
                left_min[i] = left_sum

        min_heap = []
        right_sum = 0
        for i in range(n3 - 1, -1, -1):
            heappush(min_heap, nums[i])
            right_sum += nums[i]
            if len(min_heap) > n:
                right_sum -= heappop(min_heap)
            if i <= n3 - n:
                right_min[i] = right_sum
        
        res = float('inf')
        for i in range(n - 1, n3 - n):
            res = min(res, left_min[i] - right_min[i + 1])
        return res
        
