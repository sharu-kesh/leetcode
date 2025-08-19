class DataStream:

    def __init__(self, value: int, k: int):
        self.q = deque()
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.q.append(num)
        n = len(self.q)
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        if n < self.k: return False
        if n > self.k:
            val = self.q.popleft()
            if val == self.value and self.count > 1:
                self.count -= 1
        return self.count == self.k
        
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)