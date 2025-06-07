from solutions.p0003_longest_substring_without_repeating_characters import Solution


def test_Longest_Substring_Without_Repeating_Characters():
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("bbbb") == 1
