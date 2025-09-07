class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        count = 0
        m = len(flowerbed)
        if m == 1:
            if flowerbed[0] == 0: return True
            return False
        if flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1
        if flowerbed[-1] == flowerbed[-2] == 0:
            flowerbed[-1] = 1
            count += 1

        for i in range(1, m - 1):
            if flowerbed[i] == flowerbed[i - 1] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
        
        return count >= n