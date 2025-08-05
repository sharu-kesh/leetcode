class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        res = ''
        for i, val in enumerate(s):
            if val == ' ':
                break
            if val in '+-':
                if i != 0:
                    break
            elif not val.isdigit(): 
                break
            res += val
        print(res)
        if res == '': 
            return 0
        if len(res) == 1 and res[0] in '+-': return 0
        if res[0] == '-':
            val = -1 * int(res[1:])
            return  val if val > -2 ** 31 else -2 ** 31
        val = int(res) 
        return val if val < 2 ** 31 - 1 else 2**31 - 1