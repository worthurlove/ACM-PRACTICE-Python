'''
leetcode系列：题号-144
Description:Given a binary tree, return the preorder traversal of its nodes' values.
Author:worthurlove
Date:2019.3.15
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None

#递归方法遍历
class recrsionSolution: 
    def __init__(self):
        self.record = []

    def preorderTraversal(self, root: TreeNode) -> list:

        self.preorderProcess(root)#调用中序遍历函数
        return self.record#返回遍历书序的数组

    def preorderProcess(self,root):
        if root != None:#节点不为空时则一直遍历

            self.record.append(root.val)#访问根节点

            self.preorderProcess(root.left)#访问左节点

            self.preorderProcess(root.right)#访问右节点

        else:
            return

#使用栈的非递归方法
class noRecrsionSolutopn:
    def preorderTraversal(self,root):

        if not root:#节点为空则直接返回
            return []

        stackNode = [root]
        record = []

        while stackNode:

            #出栈，访问栈顶节点
            a = stackNode.pop()
            record.append(a.val)

            #右节点先入栈，但是后出栈
            if a.right:
                stackNode.append(a.right)
            #左节点后入栈，但是先出
            if a.left:
                stackNode.append(a.left)

        return record




