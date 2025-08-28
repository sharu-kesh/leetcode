class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        n = len(mat)
        if mat == target: return True

        def rotate():
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            l = 0
            r = n - 1

            while l < r:
                for i in range(n):
                    mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
                l += 1
                r -= 1
        
        count = 0
        while count < 3:
            rotate()
            if mat == target: return True
            count += 1
        return False
        