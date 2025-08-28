class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        def sortDiagonal(row, col):
            arr = []
            i, j = row, col
            while i < n and j < m:
                arr.append(mat[i][j])
                i += 1
                j += 1
            
            arr.sort()
            k = len(arr)
            idx = 0

            while idx < k:
                mat[row][col] = arr[idx]
                idx += 1
                row += 1
                col += 1
        
        for i in range(n - 1):
            sortDiagonal(i, 0)
        
        for j in range(1, m - 1):
            sortDiagonal(0, j)
        
        return mat
        