from solutions.p0056_merge_intervals import Solution


def test_Merge_Intervals():
    s = Solution()
    assert s.merge([[4, 6], [3, 7], [1, 5]]) == [[1, 7]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
