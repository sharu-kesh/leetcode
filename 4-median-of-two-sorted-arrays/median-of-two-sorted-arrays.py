class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(B) < len(A):
            A, B = B, A
        n, m = len(A), len(B)
        tot = n + m
        mini = float('-inf')
        maxi = float('inf')

        half = tot // 2
        l = 0
        r = n - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else mini
            Aright = A[i + 1] if (i + 1) < n else maxi
            Bleft = B[j] if j >= 0 else mini
            Bright = B[j + 1] if (j + 1) < m else maxi

            if Aleft <= Bright and Bleft <= Aright:
                if tot & 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
