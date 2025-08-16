class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        i = 0
        n = len(num)
        while i < n and num[i] == '9':
            i += 1
        if i < n:
            num[i] = '9'
        return int(''.join(num))
        