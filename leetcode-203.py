'''
leetcode系列：题号-203
Description:Remove all elements from a linked list of integers that have value val.
Author:worthurlove
Date:2019.4.11
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #记录前一个节点，删除时用来连接,同时保留头结点来访问链表
        s = t = head
        while head != None:
            if head.val == val:
                if head == s:
                    head = head.next
                    s = t = head
                else:
                    s.next = head.next
                    head = head.next
            else:
                s = head
                head = head.next
        return t