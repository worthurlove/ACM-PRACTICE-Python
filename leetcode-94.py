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

#递归方法中序遍历二叉树
class recursionSolution: 
    def __init__(self):
        self.stackNode = []#定义栈来存储节点
        self.record = []

    def inorderTraversal(self, root: TreeNode) -> list:

        self.inorderProcess(root)#调用中序遍历函数
        return self.record#返回遍历书序的数组

    def inorderProcess(self,root):
        if root:#节点不为空时则一直将左节点入栈
            self.stackNode.append(root)
            self.inorderProcess(root.left)

        else:#当没有左子节点时，则出栈一个节点，
            '''
            最困惑的一点：当右边节点为空时，并不会结束遍历，会直接出栈一个节点，继续遍历；右边节点不为空时则将右子树当成根节点来遍历
                        然后出栈，接着遍历回根节点，完成中序遍历
            '''
            if self.stackNode:#栈空了则结束遍历
                b = self.stackNode.pop()
                self.record.append(b.val)
                self.inorderProcess(b.right)#会遍历出栈那个节点的右节点

#非递归方法中序遍历二叉树
class noRecursionSolution1:
    def inorderTraversal(self,root: TreeNode) -> TreeNode:
        if not root:
            return []

        stackNode = [root]

        record = []

        recordNode = []#记录已经访问过出栈的元素

        while stackNode:#栈非空时

            a = stackNode[-1]
            if a.left and a.left not in recordNode:#如果栈顶元素左节点非空且没有被访问过则入栈
                stackNode.append(a.left)

            else:
                #否则，出栈，并记录，然后如果右节点非空则入栈
                b = stackNode.pop()
                recordNode.append(b)
                record.append(b.val)
                if b.right:
                    stackNode.append(b.right)
        return record

    
#非递归方法中序遍历二叉树
class noRecursionSolution2:
    def inorderTraversal(self,root: TreeNode) -> TreeNode:
        if not root:
            return []
        
        record , stackNode = [], []
        while stackNode or root:

            if root:
                stackNode.append(root)
                root = root.left

            else:
                b = stackNode.pop()
                record.append(b.val)
                root = b.right

        return record



