class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRow = maxCol = 0
        for i, j in stones:
            maxRow = max(maxRow, i)
            maxCol = max(maxCol, j)
        
        parent = list(range(maxRow + maxCol + 2))
        rank = [1] * (maxRow + maxCol + 2)
        
        def find(x):
            res = x
            while res != parent[res]:
                parent[res] = parent[parent[res]]  # path compression
                res = parent[res]
            return res

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        mpp = {}
        res = len(stones)
        for i, j in stones:
            col = j + maxRow + 1
            union(i, col)
            mpp[i] = 1
            mpp[col] = 1
        print(parent, rank, res)
        count = 0
        for i in mpp:
            if find(i) == i:
                count += 1
        return res - count
