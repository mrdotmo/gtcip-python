from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        LeetCode Problem 19: Remove Nth Node From End Of List
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        """
        if not head:
            return None

        curr, ahead = head, head

        for _ in range(n):
            if ahead is not None:
                ahead = ahead.next

        if not ahead:
            return head.next

        while ahead.next:
            if curr:
                curr = curr.next
            if ahead:
                ahead = ahead.next

        if curr and curr.next:
            curr.next = curr.next.next

        return head
