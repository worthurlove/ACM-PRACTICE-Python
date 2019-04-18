'''
leetcode系列：题号-134
Description:Given a linked list, determine if it has a cycle in it.
            To represent a cycle in the given linked list,
             we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Author:worthurlove
Date:2019.4.18

检查链表中是否有环，通过设置两个两个指针，一个快指针，一个慢指针，快指针每次比慢的多走一步
如果存在环，则快指针一定会在一个环内的时间追上慢指针
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        if head != None and head.next != None:
            fast = head.next
        else:
            return False
        while(head!=None and head.next!=None and head.next.next!=None):
            
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
                head = fast

        return False