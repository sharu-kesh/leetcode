class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        new_intervals = []
        nums.sort()
        i = 0
        n = len(nums)
        while i < n:
            start, end = nums[i]
            j = i + 1
            while j < n and end >= nums[j][0]:
                start = min(start, nums[j][0])
                end = max(end, nums[j][1])
                j += 1
            i = j
            new_intervals.append([start, end])
        count = 0
        # print(new_intervals)
        for start, end in new_intervals:
            count += end - start + 1
        return count
        