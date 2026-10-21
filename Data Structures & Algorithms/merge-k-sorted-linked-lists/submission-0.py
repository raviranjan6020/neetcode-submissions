# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Brute force
        # Store all in a array and sort it and create new linked list and return it's head
        # Space O(n), time nlog(n)
        nums=[]
        for i in range(len(lists)):
            head=lists[i]
            while head:
                nums.append(head.val)
                head=head.next
        nums.sort()
        dummy=ListNode(0)
        head=dummy
        for num in nums:
            head.next=ListNode(num)
            head=head.next
        return dummy.next

        