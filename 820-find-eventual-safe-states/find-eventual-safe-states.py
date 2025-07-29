class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n
        path = [0] * n

        def dfs(i):
            vis[i] = 1
            path[i] = 1

            for nei in graph[i]:
                if not vis[nei]:
                    if not dfs(nei):
                        return False
                elif path[nei] == 1:
                    return False
            path[i] = 0
            return True
        res = []
        for i in range(n):
            if not vis[i]:
                dfs(i)
        for i, val in enumerate(path):
            if not val:
                res.append(i)
        return res
        