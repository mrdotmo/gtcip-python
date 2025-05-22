from solutions.p0125_Valid_Palindrome import Solution


def test_Valid_Palindrome():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama")
    assert not s.isPalindrome("race a car")
    assert s.isPalindrome(" ")
