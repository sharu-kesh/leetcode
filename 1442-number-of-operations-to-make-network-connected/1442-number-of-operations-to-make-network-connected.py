class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        if m < n - 1: return -1
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
        res = n - 1
        for i, j in connections:
            res-=union(i,j)
        return res
        