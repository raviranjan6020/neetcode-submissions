"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # two pass solution
        # copy linked list without and random value
        # have a map of old <--> new mapping
        # end pass to get random mapping and assign to newly linkedlist
        temp=head
        headrdm=Node(0)
        tempcpy=headrdm
        oldNewMapp={}
        while temp:
            newnode=Node(temp.val)
            tempcpy.next=newnode
            oldNewMapp[temp]=tempcpy.next
            temp=temp.next
            tempcpy=tempcpy.next
        temp=head
        tempcpy=headrdm.next
        while temp:
            if temp.random:
                newrandom=oldNewMapp[temp.random]
                tempcpy.random=newrandom
            temp=temp.next
            tempcpy=tempcpy.next
        return headrdm.next

        

        