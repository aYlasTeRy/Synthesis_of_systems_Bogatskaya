# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        s = ''
        while current:
            s += str(current.val)
            current = current.next
        flag = False
        if s == s[::-1]:
            flag = True

        return flag
