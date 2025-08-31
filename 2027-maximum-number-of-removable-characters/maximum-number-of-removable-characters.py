class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n, m = len(s), len(p)

        def isSubSequence(seen):
            i = 0
            j = 0

            while i < n and j < m:
                if i not in seen and s[i] == p[j]:
                    j += 1
                i += 1
            return j == m

        l = 0
        r = len(removable) - 1

        while l <= r:
            mid = (l + r) // 2
            if isSubSequence(set(removable[:mid+1])):
                l = mid + 1
            else:
                r = mid - 1
        return l
        