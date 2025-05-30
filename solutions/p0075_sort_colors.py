from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        LeetCode Problem 75: Sort Colors
        https://leetcode.com/problems/sort-colors/
        """
        curr, left = 0, 0
        right = len(nums) - 1
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                curr += 1
                left += 1
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            else:
                curr += 1
