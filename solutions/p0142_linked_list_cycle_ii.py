from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        LeetCode Problem 142: Linked List Cycle Ii
        https://leetcode.com/problems/linked-list-cycle-ii
        """
        slow = head
        fast = head
        while True:
            if slow:
                slow = slow.next
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            if slow is fast:
                break
        slow = head
        while slow is not fast:
            if slow:
                slow = slow.next
            if fast:
                fast = fast.next
        return slow
