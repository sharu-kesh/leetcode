class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        if n == 1: return grid

        def sortDiagonals(row, col, rev = True):
            arr = []
            i = row
            j = col
            while i < n and j < n:
                arr.append(grid[i][j])
                i += 1
                j += 1
            arr.sort(reverse = rev)
            k = len(arr)
            idx = 0
            while idx < k:
                grid[row][col] = arr[idx]
                idx += 1
                row += 1
                col += 1

        for i in range(n - 1):
            sortDiagonals(i, 0)
        
        for j in range(1, n - 1):
            sortDiagonals(0, j, False)
        
        return grid
        