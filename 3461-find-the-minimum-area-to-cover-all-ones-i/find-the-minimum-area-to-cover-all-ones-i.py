class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        top = left = 1001
        down = right = -1
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    top = min(top, i)
                    left = min(left, j)
                    right = max(right, j)
                    down = max(down, i)
        return ((down - top) + 1) * ((right - left) + 1)
        