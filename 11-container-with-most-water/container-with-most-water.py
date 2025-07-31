class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxi = 0
        l = 0
        r = n - 1
        while l < r:
            maxi = max(maxi, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxi
        