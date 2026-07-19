from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        vis = set()
        for i in s:
            freq[i] -= 1
            if i in vis: continue

            while stack and i < stack[-1] and freq[stack[-1]] > 0:
                vis.remove(stack.pop())
            stack.append(i)
            vis.add(i)
        return ''.join(stack)
        