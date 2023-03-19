# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = ''
        while head:
            l += str(head.val)
            head = head.next
        return int(l, 2)