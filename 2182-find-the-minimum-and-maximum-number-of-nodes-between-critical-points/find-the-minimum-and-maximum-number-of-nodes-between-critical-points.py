# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = last = 0
        pre = head
        head = head.next
        count = 2
        mini = float('inf')
        maxi = float('-inf')
        while head.next:
            if (head.val > pre.val and head.val > head.next.val) or (head.val < pre.val and head.val < head.next.val):
                if first == 0:
                    first = count
                else:
                    pre = first if not last else last
                    last = count
                    mini = min(mini, last - pre)
            # print(first, last)
            pre = head
            count += 1
            head = head.next
        if not last: return [-1, -1]
        return [mini, last - first]
        