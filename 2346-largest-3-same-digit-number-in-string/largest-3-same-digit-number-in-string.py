class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxi = '-1'
        prev = num[0]
        count = 1
        n = len(num)
        for i in range(1, n):
            if num[i] == prev:
                count += 1
                if count == 3:
                    maxi = max(maxi, prev)
                    count = 1
            else:
                prev = num[i]
                count = 1
        if maxi == '-1': return ''
        return ''.join(maxi * 3)
        