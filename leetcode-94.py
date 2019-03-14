'''
leetcode系列：题号-94
Description:Given a binary tree, return the inorder traversal of its nodes' values.
Author:worthurlove
Date:2019.3.15
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None

class solution: 
    def __init__(self):
        self.stackNode = []#定义栈来存储节点
        self.record = []

    def inorderTraversal(self, root: TreeNode) -> list:

        self.inorderProcess(root)#调用中序遍历函数
        return self.record#返回遍历书序的数组

    def inorderProcess(self,root):
        if root != None:#节点不为空时则一直将左节点入栈
            self.stackNode.append(root)
            self.inorderProcess(root.left)

        else:#当没有左子节点时，则出栈一个节点，
            '''
            最困惑的一点：当右边节点为空时，并不会结束遍历，会直接出栈一个节点，继续遍历；右边节点不为空时则将右子树当成根节点来遍历
                        然后出栈，接着遍历回根节点，完成中序遍历
            '''
            if len(self.stackNode) != 0:#栈空了则结束遍历
                b = self.stackNode.pop()
                self.record.append(b.val)
                self.inorderProcess(b.right)#会遍历出栈那个节点的右节点




