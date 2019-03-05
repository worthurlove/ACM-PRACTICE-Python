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
#解法二：Floyd算法直接求出多源最短路径
import numpy as np
N,M = map(int,input().split())

#定义点与点之间的连通矩阵即边
access_point_to_point = np.zeros((N + 1,N + 1),dtype = np.int)

for i in range(1,N + 1):
    for j in range(1,N + 1):
        access_point_to_point[i][j] = 99999

for i in range(M):#输入边，记录在矩阵中
    d1,d2 = map(int,input().split())
    access_point_to_point[d1][d2] = access_point_to_point[d2][d1] = 1


#核心代码，三重迭代直接求出最短距离矩阵
for i in range(1,N + 1):
    for j in range(1,N + 1):
        for k in range(1,N + 1):
            if (access_point_to_point[j][i] + access_point_to_point[i][k] < access_point_to_point[j][k]):
                access_point_to_point[j][k] = access_point_to_point[j][i] + access_point_to_point[i][k]


for i in range(1,N + 1):
        NUM = 0
        for j in range(1,N + 1):
                if access_point_to_point[i][j] <= 6:
                        NUM += 1
        print("{}: {:.2f}%".format(i,NUM/N*100))

                