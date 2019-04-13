'''
Description:一个1-n的顺序数列，每次从后面选取一个元素放到前端
            现在给定一个乱序，求最少多少次移动能够得到该序列
Author:worthurlov
Date:2019.4.13
'''


'''
解题思路：n减去序列末尾的升序即为最小移动次数
'''

N = int(input())

s = []
s.extend(map(int,input().split()))

#还原操作，将第一个数插入后面的数中，使其有序

num = 1
for j in range(N - 2,-1,-1):
    if s[j] < s[j + 1]:
        num += 1

 
print(N - num)
