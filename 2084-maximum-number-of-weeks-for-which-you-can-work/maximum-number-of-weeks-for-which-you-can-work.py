class Solution:
    def numberOfWeeks(self, arr: List[int]) -> int:
        sumi, maxi = sum(arr), max(arr)
        if sumi - maxi >= maxi:
            return sumi
        return 2 * (sumi - maxi) + 1