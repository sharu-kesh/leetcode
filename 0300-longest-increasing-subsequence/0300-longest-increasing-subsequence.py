class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if temp[-1] < nums[i]:
                temp.append(nums[i])
            else:
                idx = bisect_left(temp, nums[i])
                temp[idx] = nums[i]
        return len(temp)