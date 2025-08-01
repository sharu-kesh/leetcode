class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        parent=[i for i in range(n)]
        rank=[1]*n
        def find(x):
            res=x
            while res!=parent[res]:
                parent[res]=parent[parent[res]]
                res=parent[res]
            return res
        def union(x,y):
            p1,p2=find(x),find(y)
            if p1==p2: return 0
            if rank[p1]>rank[p2]:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            else: 
                parent[p2]=p1
                rank[p1]+=rank[p2]
            return 1
        res=n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    res-=union(i,j)
        return res

        