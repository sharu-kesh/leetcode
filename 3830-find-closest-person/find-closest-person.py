class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if x > z: step1 = -1
        else: step1 = 1
        if y > z: step2 = -1
        else: step2 = 1

        while True:
            if x == z and y == z:
                return 0
            if x == z:
                return 1
            if y == z:
                return 2
            x += step1
            y += step2
        