from solutions.p0015_3Sum import Solution

def test_3Sum():
    s = Solution()

    assert [[-4, 1, 3]] == s.threeSum([1, 2, -4, 3])
    assert [[0, 0, 0]] == s.threeSum([0,0, 0, 0])
    assert [[-1,-1,2],[-1,0,1]] == s.threeSum([-1, 0, 1, 2, -1, -4])
    assert [[-1,-1,2],[-1,0,1]] == s.threeSum([-1,0,1,2,-1,-4])
