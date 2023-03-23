# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        current_1 = head
        if head == None:
            return head
        while current_1 and current_1.val == val:
            head = current_1.next
            current_1 = head
        if current_1:
            while current_1.next:
                if current_1.next.val == val:
                    current_1.next = current_1.next.next
                else:
                    current_1 = current_1.next


        return head