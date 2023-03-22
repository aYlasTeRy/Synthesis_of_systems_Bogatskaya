# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current_1 = head
        current_2 = head.next
        suma = 0
        while current_2:
            if current_2.val != 0:
                suma += current_2.val
                current_2 = current_2.next

            else:
                current_2.val = suma
                current_1.next = current_2
                current_1 = current_1.next
                current_2 = current_2.next
                suma = 0

        return head.next