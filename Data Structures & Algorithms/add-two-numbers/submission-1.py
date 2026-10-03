# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0)
        t=dummy
        while l1 or l2:
            if l1 and l2:
                curr=l1.val + l2.val + carry
                carry= curr // 10
                curr = curr % 10
                l1, l2= l1.next, l2.next
            elif l1:
                curr=l1.val  + carry
                carry= curr // 10
                curr = curr % 10
                l1= l1.next
            else:
                curr=l2.val + carry
                carry= curr // 10
                curr = curr % 10
                l2 = l2.next
            t.next=ListNode(curr)
            t=t.next
        if carry: 
            t.next=ListNode(carry)
        return dummy.next



        