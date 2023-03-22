# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        current = head
        count = count // 2 + 1
        i = 0
        while current:
            i += 1
            if i == count:
                return current
            current = current.next