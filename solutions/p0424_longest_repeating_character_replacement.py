from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        LeetCode Problem 424: Longest Repeating Character Replacement
        https://leetcode.com/problems/longest-repeating-character-replacement/
        """
        freq_map = defaultdict(int)
        for i in range(k):
            freq_map[s[i]] += 1
        left, right = 0, k

        def is_valid():
            c = max(freq_map.values())
            return right - left + 1 - c <= k

        while right < len(s):
            freq_map[s[right]] += 1
            if not is_valid():
                freq_map[s[left]] -= 1
                left += 1
            right += 1
        return right - left
