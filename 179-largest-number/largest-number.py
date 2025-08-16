class Solution:
    def largestNumber(self, arr: List[int]) -> str:
        def cmp(a, b):
            if a + b > b + a: return -1
            elif b + a > a + b: return 1
            else: return 0

        arr = sorted(list(map(str, arr)), key = cmp_to_key(cmp))
        res = ''.join(arr)
        return '0' if res[0] == '0' else res