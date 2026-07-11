from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        vis = [0] * n
        components = 0

        def countComponent(node):
            nodeCount = 1
            edgeCount = 0
            vis[node] = 1
            q = deque([node])

            while q:
                cur = q.popleft()
                edgeCount += len(adj[cur])
                for adjnode in adj[cur]:
                    if not vis[adjnode]:
                        vis[adjnode] = 1
                        nodeCount += 1
                        q.append(adjnode)
            edgeCount //= 2
            # print(nodeCount, edgeCount)
            return edgeCount == (nodeCount * (nodeCount - 1)) // 2

        for i in range(n):
            if not vis[i]:
                val = countComponent(i)
                components += val
        return components
        