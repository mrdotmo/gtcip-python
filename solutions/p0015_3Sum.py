from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        LeetCode Problem 15: 3Sum
        https://leetcode.com/problems/3sum
        """
        nums.sort()
        rv = []

        prev = nums[0] - 1
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if prev == nums[i]:
                continue
            prev = nums[i]
            low, high = i + 1, len(nums) - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    rv.append([nums[i], nums[low], nums[high]])
                    low += 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    high -= 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

        return rv
