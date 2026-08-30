# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        ptr = dummy
        cnt = 0

        while ptr.next:
            if cnt >= n:
                prev = prev.next
            
            ptr = ptr.next
            cnt += 1
        
        if prev.next is None:
            return None
        else:
            prev.next = prev.next.next
        
        return dummy.next
