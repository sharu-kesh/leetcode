class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        curSum = 0
        count = 0
        s = set()
        for num in nums:
            if num < 0:
                count += 1
                continue
            if num not in s:
                curSum += num
            s.add(num)
        return curSum if count != len(nums) else max(nums)
