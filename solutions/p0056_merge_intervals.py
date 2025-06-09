from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        LeetCode Problem 56: Merge Intervals
        https://leetcode.com/problems/merge-intervals/
        """
        intervals.sort(key=lambda x: x[0])
        current_start, current_end = intervals[0][0], intervals[0][1]
        rv: List[List[int]] = []

        for i in range(1, len(intervals)):
            next_interval = intervals[i]
            if next_interval[0] <= current_end:
                current_end = max(next_interval[1], current_end)
            else:
                rv.append([current_start, current_end])
                current_start, current_end = next_interval[0], next_interval[1]
        rv.append([current_start, current_end])
        return rv
