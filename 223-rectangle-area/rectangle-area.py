class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        def area(x1, y1, x2, y2):
            l = abs(x1 - x2)
            w = abs(y1 - y2)

            return l * w
        

        a1 = area(ax1, ay1, ax2, ay2)
        a2 = area(bx1, by1, bx2, by2)

        overlap_width = max(0, min(ax2,bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        a3 = overlap_height * overlap_width

        return a1 + a2 - a3

        