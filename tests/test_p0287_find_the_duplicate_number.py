from solutions.p0287_find_the_duplicate_number import Solution


def test_Find_The_Duplicate_Number():
    s = Solution()
    assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert s.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert s.findDuplicate([3, 3, 3, 3, 3]) == 3
    assert s.findDuplicate([4, 3, 1, 4, 2]) == 4
