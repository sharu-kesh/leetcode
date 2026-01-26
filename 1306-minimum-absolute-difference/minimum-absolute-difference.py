from collections import defaultdict
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        di = defaultdict(list)
        arr.sort()
        n = len(arr)
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            di[diff].append([arr[i - 1], arr[i]])
        
        return di[min(di)]
        