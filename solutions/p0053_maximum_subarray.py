from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        LeetCode Problem 53: Maximum Subarray
        https://leetcode.com/problems/maximum-subarray/
        """
        sum: int = -(10**4 + 1)
        max_val: int = -(10**4 + 1)

        for v in nums:
            sum = max(sum + v, v)
            max_val = sum if sum > max_val else max_val
        return max_val
