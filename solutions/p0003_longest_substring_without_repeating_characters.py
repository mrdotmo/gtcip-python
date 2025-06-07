from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        LeetCode Problem 3: Longest Substring Without Repeating Characters
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
        """
        freq_map = defaultdict(int)
        left, right = 0, 0

        rv = 0
        while right < len(s):
            freq_map[s[right]] += 1
            while freq_map[s[right]] > 1:
                freq_map[s[left]] -= 1
                left += 1
            rv = max(rv, right - left + 1)
            right += 1
        return rv
