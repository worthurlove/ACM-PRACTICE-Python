'''
PAT数据结构题目：堆的路径

Description：将一系列给定数字插入一个初始为空的小顶堆H[]。随后对任意给定的下标i，打印从H[i]到根结点的路径。
            输入格式:
            每组测试第1行包含2个正整数N和M(≤1000)，分别是插入元素的个数、以及需要打印的路径条数。下一行给出区间[-10000, 10000]内的N个要被插入一个初始为空的小顶堆的整数。最后一行给出M个下标。

            输出格式:
            对输入中给出的每个下标i，在一行中输出从H[i]到根结点的路径上的数据。数字间以1个空格分隔，行末不得有多余空格。

Author:worthurlove

Date:2019.3.5
'''
#核心内容，堆的初始化，堆的查找
#用数组存储堆，将数组中元素调整为小根堆或者一个一个插入后调整为小顶堆（本题中使用插入调整的方法）
N,M = map(int,input().split())

min_heap = [0]*N#将小根堆初始化为空，第0个元素用于交换的中间点

# for i in range(N):8
#     cur = int(input())
#     min_heap.append(cur)
min_heap[1:N] = map(int,input().split())



#初始化小根堆
for i in range(1,N + 1):

    k = i#新插入的元素在数组中的位置

    min_heap[0] = min_heap[k]#保存被置换出来的那个节点

    father_point = int(k/2)

    while (father_point > 0) and (min_heap[father_point] > min_heap[0]):
        min_heap[k] = min_heap[father_point]
        k = father_point
        father_point = int(k/2)

    min_heap[k] = min_heap[0]


#输入起始点
start_point = [0]*M
start_point[:M] = map(int,input().split())

for i in range(M):
    while start_point[i] != 0:
        if start_point[i] == 1:
            print(min_heap[start_point[i]])
        else:
            print(min_heap[start_point[i]],end = ' ')
        start_point[i] = int(start_point[i]/2)
