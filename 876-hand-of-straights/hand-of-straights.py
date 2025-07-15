class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        freq = Counter(hand)
        minH = list(freq.keys())
        heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in freq: return False
                freq[i] -= 1
                if not freq[i]:
                    if i != minH[0]: return False
                    heappop(minH)
        return True
        