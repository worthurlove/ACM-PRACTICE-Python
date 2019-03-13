'''
leetcode系列：题号-82
Description:Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Author:worthurlove
Date:2019.3.13
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class solution:
    def DeleteAllDuplicateNode(self,head: ListNode) -> ListNode:

        theOne = {}#定义字典，先遍历一次链表记录每个元素出现的次数

        cur = head

        #先遍历一遍链表统计每个元素的个数
        while cur != None:

            if cur.val not in theOne.keys():#该元素不在字典里时，加入字典，出现次数初始化为1
                theOne[cur.val] = 1

            else:#已经在字典里时，则个数加1
                theOne[cur.val] += 1

            cur = cur.next

        #由于链表没有头结点，所以需要考虑首部节点的特殊情况
        while head != None:
            if theOne[head.val] >= 2:
                head = head.next
            else:
                break

        cur = front = head#定义当前节点和前面节点，用于删除元素

        while cur != None:
            if theOne[cur.val] == 1:#在字典里的记录数只有1说明没有重复，直接下一个
                front = cur
                cur  = cur.next

            else:#否则将该节点删除
                front.next = cur.next
                cur = cur.next
            
        return head