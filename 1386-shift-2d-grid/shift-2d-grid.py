class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        res = []
        for i in grid:
            for j in i:
                res.append(j)
        leng = m * n
        res[:leng - k] = reversed(res[:leng - k])
        res[leng - k: ] = reversed(res[leng - k:])
        res = res[::-1]
        l = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = res[l]
                l += 1
        return grid
