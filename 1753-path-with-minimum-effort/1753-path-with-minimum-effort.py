class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        minH = [(0, 0, 0)]
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0
        while minH:
            weight, i, j = heappop(minH)
            dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in dir:
                r, c = i + dr, j + dc
                if 0 <= r < n and 0 <= c < m:
                    new_weight = max(weight, abs(heights[i][j] - heights[r][c]))
                    if new_weight < dist[r][c]:
                        heappush(minH, (new_weight, r, c))
                        dist[r][c] = new_weight
        return dist[-1][-1]
            
        