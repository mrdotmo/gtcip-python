from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        LeetCode Problem 457: Circular Array Loop
        https://leetcode.com/problems/circular-array-loop/
        """
        def next_index(i: int) -> int:
            return (i + nums[i]) % len(nums)

        dead = 0
        for i in range(len(nums)):
            if nums[i] == dead:
                continue
            slow = i
            fast = next_index(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
                if slow == fast:
                    if slow != next_index(fast):
                        breakpoint()
                        return True
                    break
                slow = next_index(slow)
                fast = next_index(next_index(fast))
            j = i
            while nums[j] * nums[next_index(j)] > 0:
                k = next_index(j)
                nums[j] = dead
                j = k
        return False
