class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = {}
        stack = []
        n = len(nums2)
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack: s[nums2[i]] = stack[-1]
            else:
                s[nums2[i]] = -1
            stack.append(nums2[i])
        res = []
        for i in nums1:
            res.append(s[i])
        return res 