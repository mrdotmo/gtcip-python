from solutions.p0457_circular_array_loop import Solution


def test_Circular_Array_Loop():
    s = Solution()

    assert s.circularArrayLoop([2, -1, 1, 2, 2])
    assert s.circularArrayLoop([1, -1, 5, 1, 4])
    assert not s.circularArrayLoop([2, 2, 2, 2, 2, 4, 7])
    assert not s.circularArrayLoop([-1, -2, -3, -4, -5, 6])
    assert not s.circularArrayLoop([-1, -2, -3, -4, -5])
