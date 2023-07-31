class Solution:
    def intersection(self, head):
        slow, fast = head, head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        
        return 0
    
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        
        intersectionPoint = self.intersection(head)
        if not intersectionPoint:
            return
        
        start = head
        
        while start != intersectionPoint:
            start = start.next
            intersectionPoint = intersectionPoint.next
        
        return start