from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        LeetCode Problem 287: Find The Duplicate Number
        https://leetcode.com/problems/find-the-duplicate-number/
        """
        slow, fast = nums[0], nums[0]
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
