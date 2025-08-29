class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use indices as markers

        # for i in nums:
        #     i = abs(i)
        #     if nums[i - 1] < 0:
        #         return i
        #     nums[i - 1] = -1 * nums[i - 1]

        # use bytearray to mark the elements that are visited

        # seen = bytearray(len(nums) + 1)
        # for i in nums:
        #     if seen[i]:
        #         return i
        #     seen[i] = 1

        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow