# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        level = 1
        q = deque([root])
        maxi = float('-inf')
        cur_level = 1
        while q:
            sumi = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                sumi += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if sumi > maxi:
                maxi = sumi
                level = cur_level
            cur_level += 1
        return level
                
        