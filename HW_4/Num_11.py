# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return True
        prev = None

        cur1 = head
        cur2 = head.next

        while cur2 and cur2.next:
            cur1 = cur1.next
            cur2 = cur2.next.next

        while cur1:
            nxt = cur1.next
            cur1.next = prev
            prev = cur1
            cur1 = nxt

        while prev and head:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
