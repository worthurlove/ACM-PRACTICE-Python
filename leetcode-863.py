'''
leetcode系列：题号-863
Description:We are given a binary tree (with root node root), a target node, and an integer value K.

            Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order
Author:worthurlove
Date:2019.5.14
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]RE
        """
        '''
        将二叉树转换为无向图，再利用广度优先遍历求单源最短距离
        '''
        nodeQueue = [root]

        num = 500


        nodeGraph = [[] for i in range(num+1)]

        nodeQueue = [root]
        while nodeQueue:
            tmp = nodeQueue.pop(0)
            if tmp.left:
                nodeQueue.append(tmp.left)
                nodeGraph[tmp.val].append(tmp.left.val)
                nodeGraph[tmp.left.val].append(tmp.val)
            if tmp.right:
                nodeQueue.append(tmp.right)
                nodeGraph[tmp.val].append(tmp.right.val)
                nodeGraph[tmp.right.val].append(tmp.val)
        #print(nodeGraph)     

        '''
        广度优先遍历
        '''         
        distance = [-1]*num

        visited = [0]*num

        start = target.val

        visited[start] = 1

        queueBFS = [start]
        last = []


        d = 1
        distance[start] = 0
        while queueBFS:
            last = queueBFS.copy()
            while queueBFS:
                tmp = queueBFS.pop(0)
                for i in nodeGraph[tmp]:
                    if visited[i] == 0:
                        distance[i] = d
                    
            for j in last:
                for i in nodeGraph[j]:
                    if visited[i] == 0:
                        queueBFS.append(i)
                        visited[i] = 1
            d += 1

        #print(distance)
        reValue = []
        for i in range(num):
            if distance[i] == K:
                reValue.append(i)
                
        return reValue
   


root = TreeNode(3)

node5 = TreeNode(5)

node1 = TreeNode(1)

node6 = TreeNode(6)

node2 = TreeNode(2)

node0 = TreeNode(0)

node8 = TreeNode(8)

node7 = TreeNode(7)

node4 = TreeNode(4)

root.left = node5
root.right = node1

node5.left = node6
node5.right = node2

node2.left  = node7
node2.right = node4

node1.left = node0
node1.right = node8

result = Solution()

result.distanceK(root,node5,2)