# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, cur, temp = None, head, None

        while cur: 

            # save next first

            temp = cur.next

            # current point to prev 

            cur.next = prev 
            
            prev = cur 

            cur = temp

        
        # for the last case, cur is now set to Null;
        # prev is set to the last node, which is thus the head

        return prev
        