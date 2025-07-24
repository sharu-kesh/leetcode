class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        maxi = max(left) if left else 0
        mini = n - min(right) if right else 0
        return max(maxi, mini)