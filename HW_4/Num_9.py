# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        current_A = headA
        current_B = headB

        count_A = 0
        count_B = 0
        while current_A:
            count_A += 1
            current_A = current_A.next
        while current_B:
            count_B += 1
            current_B = current_B.next

        current_A = headA
        current_B = headB

        if count_A > count_B:
            count_C = count_A - count_B
            for i in range(count_C):
                current_A = current_A.next
        elif count_A < count_B:
            count_C = count_B - count_A
            for i in range(count_C):
                current_B = current_B.next

        while current_A and current_B:
            if current_A == current_B:
                return current_A
            else:
                current_A = current_A.next
                current_B = current_B.next

        return None