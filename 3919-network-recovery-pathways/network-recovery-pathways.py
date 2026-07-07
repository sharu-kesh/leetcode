from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        valid = set(i for i, x in enumerate(online) if not x)
        n = len(online)
        adj = defaultdict(list)
        weights = []

        for u, v, w in edges:
            if u in valid or v in valid: continue
            adj[u].append((v, w))
            weights.append(w)
        
        if not weights: return -1
        weights = sorted(set(weights))
        
        def check(limit):
            dist = [float('inf')] * n
            dist[0] = 0

            pq = [(0, 0)]
            while pq:
                cost, node = heappop(pq)
                if cost > dist[node]: continue

                for edge, wei in adj[node]:
                    if wei < limit: continue
                    new_cost = cost + wei

                    if new_cost < dist[edge]:
                        dist[edge] = new_cost
                        heappush(pq, (new_cost, edge))
            return dist[n - 1] <= k

        low = 0
        high = len(weights) - 1
        ans = -1 

        while low <= high:
            mid = (low + high) // 2

            if check(weights[mid]):
                ans = weights[mid]
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
