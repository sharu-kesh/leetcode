from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        # min-heap: (price_so_far, stops_used, current_node)
        minH = [(0, 0, src)]
        visited = dict()  # (node, stops): cost

        while minH:
            cost, stops, node = heappop(minH)
            if node == dst:
                return cost
            if stops > k:
                continue
            for nei, price in adj[node]:
                new_cost = cost + price
                if (nei, stops) not in visited or new_cost < visited[(nei, stops)]:
                    visited[(nei, stops)] = new_cost
                    heappush(minH, (new_cost, stops + 1, nei))

        return -1