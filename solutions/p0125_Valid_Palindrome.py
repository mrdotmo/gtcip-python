class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        LeetCode Problem 125: Valid Palindrome
        https://leetcode.com/problems/valid-palindrome/
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            print(
                f"Left {s[left].lower()} at {left} and Right {s[right].lower()} and {right}"
            )
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
