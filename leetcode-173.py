

'''
leetcode系列：题号-173
Description:Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

            Calling next() will return the next smallest number in the BST
Author:worthurlove
Date:2019.5.16
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.root:
            last = tmp = self.root
            while tmp.left:
                last = tmp
                tmp = tmp.left

            if tmp == last:
                self.root = self.root.right
                return tmp.val
            else:
                last.left = tmp.right
                return tmp.val
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.root:
            return True
        else:
            return False