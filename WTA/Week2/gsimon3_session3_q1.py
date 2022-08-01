# Question 1: 

# Given k sorted linked lists, merge them into a single list in increasing order.

# input: k = 3
# A comment.
# L1 = 1->5->7->null
# L2 = 2->3->6->9->null
# L3 = 4->8->10->null

# Output: 1,2,3,4,5,6,7,8,9,10

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return None
        else:
            while len(lists) > 1:
                mergedLists = []
                
                for i in range(0, len(lists), 2):
                    l1 = lists[i]
                    l2 = lists[i+1] if (i+1) < len(lists) else None
                    mergedLists.append(self.mergeList(l1,l2))
                lists= mergedLists
            return lists[0]
        
    def mergeList(self, l1, l2):
            dummy = ListNode()
            tail = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next
                    
