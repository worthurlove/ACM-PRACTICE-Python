'''
leetcode系列：题号-83
Description:Given a sorted linked list, delete all duplicates such that each element appear only once.
Author:worthurlove
Date:2019.3.13
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        b = []#记录链表中不同的元素

        cur = tmp = head#两个链表节点，一个记录当前位置，一个记录当前位置的前一个位置

        while tmp!=None:
            if tmp.val not in b:#如果b中没有该节点的元素，说明还没有遇到重复的该元素

                b.append(tmp.val)#将该元素添加到b中，下次再出现时就是重复元素了
                
                cur = tmp#记录当前节点

                tmp = tmp.next#节点后移一个

            else:#该元素为重复元素时则删除该节点
                cur.next = tmp.next
                tmp = tmp.next
                
        return head