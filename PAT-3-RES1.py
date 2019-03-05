'''
Pat数据结构题系列：7-7，六度空间
题目描述：“六度空间”理论又称作“六度分隔（Six Degrees of Separation）”理论。这个理论可以通俗地阐述为：“你和任何一个陌生人之间所间隔的人不会超过六个，也就是说，最多通过五个人你就能够认识任何一个陌生人。

“六度空间”理论虽然得到广泛的认同，并且正在得到越来越多的应用。但是数十年来，试图验证这个理论始终是许多社会学家努力追求的目标。

然而由于历史的原因，这样的研究具有太大的局限性和困难。随着当代人的联络主要依赖于电话、短信、微信以及因特网上即时通信等工具，能够体现社交网络关系的一手数据已经逐渐使得“六度空间”理论的验证成为可能。

假如给你一个社交网络图，请你对每个节点计算符合“六度空间”理论的结点占结点总数的百分比。

输入格式:
输入第1行给出两个正整数，分别表示社交网络图的结点数N（1<N≤10^4，表示人数）、边数M（≤33×N，表示社交关系数）。随后的M行对应M条边，每行给出一对正整数，分别是该条边直接连通的两个结点的编号（节点从1到N编号）。

输出格式:
对每个结点输出与该结点距离不超过6的结点数占结点总数的百分比，精确到小数点后2位。每个结节点输出一行，格式为“结点编号:（空格）百分比%”
'''
#解法一：利用广度优先遍历算法，从每个点开始进行遍历，找出各点之间的距离
import numpy as np
N,M = map(int,input().split())

#定义点与点之间的连通矩阵即边
access_point_to_point = np.zeros((N + 1,N + 1),dtype = np.bool)

NUM_POINT = [1]*(N + 1)





#定义节点结构体:两种方法
#方法一：
distance_point_to_point = np.dtype([('distance','i4'),('editable','bool')])

graph_point_to_point = np.zeros((N + 1,N + 1),dtype = distance_point_to_point)

for i in range(N + 1):
    for j in range(N + 1):
        graph_point_to_point[i][j] = (-1,True)

# #方法二：通过类来实现
# class Graph_point(object):
#     def __init__(self,distance,editable):
#         self.distance = distance
#         self.editable = editable

# graph = np.zeros((N + 1,N + 1),dtype = Graph_point)

# for i in range(N + 1):
#     for j in range(N + 1):
#         graph[i][j] = Graph_point(-1,True)

# # print(graph[1][1].distance)#访问方式


for i in range(M):#输入边，记录在矩阵中
    d1,d2 = map(int,input().split())
    access_point_to_point[d1][d2] = access_point_to_point[d2][d1] = True


#对于每一个顶点从它开始广度优先遍历
layer_1 = []#用于存储当前层的节点
layer_2 = []#存储下一层的节点

for i in range(1,N + 1):
        visited_point = np.zeros(N+1,dtype = np.int8)#节点是否已经被访问过

        step = 1#当前遍历所在的层次
        queue_point = [i] #利用队列进行广度优先遍历
        
        layer_1.append(i)

        visited_point[i] = 1
        while len(queue_point) != 0:#队列为空时则遍历结束
                u = queue_point.pop(0)#队首出队

                layer_1.pop()


                for j in range(1,N + 1):
                        if (access_point_to_point[u][j] == True) and ( visited_point[j] != 1):#当该节点可编辑且未被访问时节点入队列

                                visited_point[j] = 1

                                queue_point.append(j)#相连的点入队列

                                layer_2.append(j)

                                if  graph_point_to_point[i][j]['editable'] == True:
                                        if step <= 6:

                                                NUM_POINT[i] += 1
                                                NUM_POINT[j] += 1
                                                
                                        graph_point_to_point[i][j]['distance'] = graph_point_to_point[j][i]['distance'] = step #对称的点也是最短距离
                                        graph_point_to_point[i][j]['editable'] = graph_point_to_point[j][i]['editable'] = False

                if len(layer_1) == 0:#当前层已经全部出队列
                        step += 1#遍历的层次加1
                        layer_1 = layer_2
                        layer_2 = []



for i in range(1,N + 1):
        print("{}: {:.2f}%".format(i,NUM_POINT[i]/N*100))

        


