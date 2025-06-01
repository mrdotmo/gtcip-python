from solutions.p0424_longest_repeating_character_replacement import Solution


def test_Longest_Repeating_Character_Replacement():
    s = Solution()
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("AABABBA", 1) == 4
