class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        def rec(num):
            if low <= num <= high:
                res.append(num)
            elif num > high: return
            val = num % 10
            if val == 9: return
            num = (num * 10) + (val + 1) 
            # print(val, num)
            rec(num)
        
        for i in range(1, 9):
            rec(i)
        return sorted(res)
        