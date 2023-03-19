# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode(0)
        head = current

        current_1 = list1
        current_2 = list2

        while current_1 and current_2:
            if current_1.val < current_2.val:
                current.next = current_1
                current_1 = current_1.next
            else:
                current.next = current_2
                current_2 = current_2.next
            current = current.next
        while current_1:
            current.next = current_1
            current_1 = current_1.next
            current = current.next
        while current_2:
            current.next = current_2
            current_2 = current_2.next
            current = current.next

        return head.next