class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        n = len(asteroids)
        for i in range(1, n):
            val = asteroids[i]
            flag = True
            while flag and stack and stack[-1] > 0 and val < 0:
                if stack[-1] < -val:
                    stack.pop()
                    continue
                if stack[-1] == -val:
                    stack.pop()
                flag = False
            if flag:
                stack.append(val)
        return stack

        