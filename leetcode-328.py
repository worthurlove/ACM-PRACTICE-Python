
'''
leetcode系列：题号-328
Description:Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

            You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
Author:worthurlove
Date:2019.4.18
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        tmp1 = None
        tmp2 = None
        if head != None:
            tmp1 = head
            if head.next != None:
                tmp2 = head.next
        else:
            return head
        odd = tmp2
        while tmp2 != None and tmp2.next != None:
            
                tmp1.next = tmp2.next
                tmp1 = tmp1.next
                if tmp1.next != None:
                    tmp2.next = tmp1.next
                    tmp2 = tmp2.next
                else:
                    tmp2.next = None
            
                
            
        tmp1.next = odd
        return head