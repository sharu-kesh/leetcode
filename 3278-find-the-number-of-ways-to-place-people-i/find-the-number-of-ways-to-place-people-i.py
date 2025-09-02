class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : (-x[0], x[1]))
        count = 0
        n = len(points)

        for i in range(n - 1):
            y = 1 << 31
            for j in range(i + 1, n):
                if y > points[j][1] >= points[i][1]:
                    count += 1
                    y = points[j][1]
        return count
        
        