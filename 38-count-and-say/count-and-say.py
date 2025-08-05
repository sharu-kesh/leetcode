class Solution:
    def countAndSay(self, n: int) -> str:
        
        def countFreq(res):
            if len(res) == 1:
                return [[res[0], '1']]
            count = 1
            arr = []
            pre = res[0]
            for i in range(1, len(res)):
                if res[i] == pre:
                    count += 1
                else:
                    arr.append([pre, str(count)])
                    pre = res[i]
                    count = 1
            if count: arr.append([pre, str(count)])
            return arr

        def mergeFreq(arr):
            s = ''
            for i, j in arr:
                s += j + i
            return s

        res = '1'

        for i in range(1, n):
            arr = countFreq(res)
            res = mergeFreq(arr)
        return res
        