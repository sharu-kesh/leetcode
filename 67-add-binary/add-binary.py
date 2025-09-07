class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res = ''
        carry = 0
        while i >= 0 or j >= 0 or carry:
            val1 = int(a[i]) if i >= 0 else 0
            val2 = int(b[j]) if j >= 0 else 0
            temp = val1 + val2 + carry
            if temp <= 1: 
                res += str(temp)
                carry = 0
            elif temp == 2:
                res += '0'
                carry = 1
            else:
                res += '1'
                carry = 1
            i -= 1
            j -= 1
        return res[::-1]
            
        