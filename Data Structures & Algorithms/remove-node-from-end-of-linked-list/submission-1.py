# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next
        
        if n == length:
            return head.next
        travel_length = (length - n) 
        count = 1
        temp = head
        while count != travel_length:
            count += 1
            temp = temp.next
        
        tmp = temp.next
        forward = temp.next.next
        temp.next = forward
        tmp.next = None

        return head

        