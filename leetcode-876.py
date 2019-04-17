'''
leetcode系列：题号-876
Description:Given a non-empty, singly linked list with head node head, return a middle node of linked list.

            If there are two middle nodes, return the second middle node.
Author:worthurlove
Date:2019.4.17
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        num = 0
        tmp = head
        while tmp:
            num += 1
            tmp = tmp.next
        
        mid = int(num/2) + 1
        
        num = 1
        while num < mid:
            head = head.next
            num += 1
            
        return head 