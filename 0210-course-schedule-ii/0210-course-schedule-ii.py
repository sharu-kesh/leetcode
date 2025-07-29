class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1: return [0]
        adj = defaultdict(list)
        stack = []
        for a, b in prerequisites:
            adj[b].append(a)
        vis = [0] * numCourses
        path = [0] * numCourses
        def dfs(i):
            vis[i] = 1
            path[i] = 1
            for nei in adj[i]:
                if not vis[nei]:
                    if not dfs(nei):
                        return False
                elif path[nei] == 1:
                    return False
            stack.append(i)
            path[i] = 0
            return True
        for i in range(numCourses):
            if not vis[i]:
                if not dfs(i):
                    return []
        return stack[::-1]

        
        