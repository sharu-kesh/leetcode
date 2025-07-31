class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = len(intervals)
        longest = 0
        intervals.sort(key = lambda x : (x[0], -x[1]))
        for start, end in intervals:
            if end <= longest:
                res -= 1
            else:
                longest = end
        return res
        