class Solution:
    def mostBooked(self, n: int, nums: List[List[int]]) -> int:
        nums.sort()
        count = [0] * n
        freeRooms = list(range(n))
        heapify(freeRooms)
        busy = []

        for start, end in nums:
            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(freeRooms, room)
            if freeRooms:
                room = heappop(freeRooms)
                heappush(busy, (end, room))
                count[room] += 1
            else:
                early, room = heappop(busy)
                heappush(busy, (early + (end - start), room))
                count[room] += 1
                
        return count.index(max(count))
            