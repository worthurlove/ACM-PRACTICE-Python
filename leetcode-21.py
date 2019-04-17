'''
leetcode系列：题号-21
Description:Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Date:2019.4.17
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        else:
            if l2.val<l1.val:
                tmp = l2
                l2 = l1
                l1 = tmp
        head = l1
        tmp1 = l1
        tmp2 = l2
        
        while l2:
            if l1.next != None:
                while l1.val <= l2.val and l1.next.val <= l2.val and l1.next != None:
                    l1 = l1.next
                    tmp1 = l1
                    if l1.next == None:
                        break
            tmp2 = l2
            
            l2 = l2.next
            
            tmpx = l1.next
            
            tmp1.next = tmp2
            
            
            
            tmp2.next = tmpx
            
            l1 = l1.next
            tmp1 = l1
            
        return head
            