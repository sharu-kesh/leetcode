class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        collisions = 0
        left = 0
        right = n - 1
        while left < n and directions[left] == 'L':
            left += 1
        while right >= 0 and directions[right] == 'R':
            right -= 1
        for i in directions[left : right + 1]:
            if i != 'S':
                collisions += 1 
        return collisions 
        