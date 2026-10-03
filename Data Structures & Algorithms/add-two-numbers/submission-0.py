# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        carry=0
        dummy=ListNode(0)
        t=dummy
        while t1 or t2:
            if t1 and t2:
                curr=t1.val + t2.val + carry
                carry= curr // 10
                curr = curr % 10
                t.next=ListNode(curr)
                t=t.next
                t1, t2= t1.next, t2.next
            elif t1:
                curr=t1.val  + carry
                carry= curr // 10
                curr = curr % 10
                t.next=ListNode(curr)
                t=t.next
                t1= t1.next
            else:
                curr=t2.val + carry
                carry= curr // 10
                curr = curr % 10
                t.next=ListNode(curr)
                t=t.next
                t2 = t2.next
        if carry: 
            t.next=ListNode(carry)
        return dummy.next



        