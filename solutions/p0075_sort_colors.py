from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        LeetCode Problem 75: Description
        https://leetcode.com/problems/sort-colors/description/
        """
        # Initliaze the position of the next Zero
        next_zero = 0
        while not nums[next_zero] and next_zero < len(nums):
            next_zero += 1
        # Initialize the position of the next Three
        next_three = len(nums) - 1
        while nums[next_three] == 3 and next_three >=0:
            next_three -= 1
        # While next zero is less then next three iterate
        curr = next_zero + 1
        while curr < next_three:
            while nums[curr] == 0:
                if nums[next_zero] == 2:
                    # swap next_zero and curr
                    pass
                if nums[next_zero] == 3:
                    # move next_zero into next_three, next_three into curr, curr into next_zero
                    # decrement next_tree
                    pass
                # increment next_zero
            # increment curr
