class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        def checkRow(row):
            s = set()
            for j in range(n):
                if board[row][j].isdigit() and board[row][j] in s:
                    return True
                s.add(board[row][j])
            return False

        def checkCol(col):
            s = set()
            for i in range(n):
                val = board[i][col]
                if val.isdigit() and val in s:
                    return True
                s.add(val)
            return False

        def checkBox(row, col):
            s = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    val = board[i][j]
                    if val.isdigit() and val in s:
                        return False
                    s.add(val)
            return True

        for i in range(n):
            if checkRow(i): return False
        
        for i in range(n):
            if checkCol(i): return False
        
        for i in range(n):
            for j in range(n):
                if i % 3 == 0 and j % 3 == 0:
                    if not checkBox(i, j):
                        return False
        
        return True
        