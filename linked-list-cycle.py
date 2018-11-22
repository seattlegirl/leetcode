#coding=utf-8
"""
给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？

快慢指针法。定义两个指针：快指针每次走一步；慢指针每次走两步。依次循环下去，如果链表存在环，那么快慢指针一定会有相等的时候。 
为了便于理解，你可以想象在操场跑步的两个人，一个快一个慢，那么他们一定会相遇（无论他们的起始点是不是在操场）。
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print Solution().hasCycle(head)
   
    
