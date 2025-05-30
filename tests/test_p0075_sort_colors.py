from solutions.p0075_sort_colors import Solution


def test_Description():
    s = Solution()

    nums = [0, 0, 0]
    s.sortColors(nums)
    assert nums == [0, 0, 0]

    nums = [2, 2, 2]
    s.sortColors(nums)
    assert nums == [2, 2, 2]

    nums = [2, 0, 2]
    s.sortColors(nums)
    assert nums == [0, 2, 2]

    nums = [1, 0, 2]
    s.sortColors(nums)
    assert nums == [0, 1, 2]

    nums = [2, 0, 1]
    s.sortColors(nums)
    assert nums == [0, 1, 2]

    nums = [0, 1, 0]
    s.sortColors(nums)
    assert nums == [0, 0, 1]

    nums = [1]
    s.sortColors(nums)
    assert nums == [1]
