from solutions.p0053_maximum_subarray import Solution


def test_maximum_subarray():
    # TODO: Implement test cases
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert s.maxSubArray([8]) == 8
    assert s.maxSubArray([-1]) == -1
