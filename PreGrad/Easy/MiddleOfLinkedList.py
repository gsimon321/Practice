# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = mid = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        point = count//2
        
        counter = 0
        while mid:
            if counter == point:
                return mid
            else:
                counter += 1
                mid = mid.next
        return None