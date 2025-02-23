# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        carry = 0

        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = l1.val + carry
                l1 = l1.next
            elif l2:
                sum = l2.val + carry 
                l2 = l2.next

            if sum >= 10:
                sum -= 10
                carry = 1
            else:
                carry = 0

            cur.next = ListNode(sum)
            cur = cur.next
        
        if carry != 0:
            cur.next = ListNode(carry)
        
        return res.next

                
        



        
