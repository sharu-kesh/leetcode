class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum = 0
        l = 0
        freq = defaultdict(int)
        n = len(nums)
        curSum = 0
        for r in range(n):
            curSum += nums[r]
            freq[nums[r]] += 1
            while freq[nums[r]] != 1:
                curSum -= nums[l]
                freq[nums[l]] -= 1
                l += 1
            # print(curSum)
            maxSum = max(maxSum, curSum)
        return maxSum
        