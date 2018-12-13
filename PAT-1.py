'''
PAT中文题系列:1008

Describe：一个数组A中存有N（>0）个整数，在不允许使用另外数组的前提下，将每个整数循环向右移M（≥0）个位置，
即将A中的数据由（A0A1⋯A​N−1）变换为（AN−M⋯AN−1A0A1⋯AN−M−1）（最后M个数循环移至最前面的M个位置）。
如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？
Author：worthurlove
Date：2018.12.13
'''
N,M = map(int,input().split())

arr_a = [0]*N


arr_a = [int(i) for i in input().split()]

M = M%N#当移动的长度大于N的时候取余，避免重复操作

#当M>=(N/2)时向左移N-M位，M<(N/2)时向右移M位

if M <= N/2:
    for i in range(M):#移动M次，可以考虑改进算法，一次移动M个位置
        #设置两个记录变量，curr记录需要移动的值，curr_next记录下一个位置的值
        curr = arr_a[0]
        curr_next = arr_a[1]
        for j in range(N):
            arr_a[(j + 1) % N] = curr#取余实现循环
            curr = curr_next
            curr_next = arr_a[(j + 2) % N]
else:
    M = N - M
    for i in range(M):#移动M次，可以考虑改进算法，一次移动M个位置
        #设置两个记录变量，curr记录需要移动的值，curr_next记录下一个位置的值
        curr = arr_a[N - 1]
        curr_next = arr_a[N - 2]
        for j in range(N - 1,-1,-1):
            arr_a[(j - 1 + N) % N] = curr#向左循环，实现方式与向右有差别
            curr = curr_next
            curr_next = arr_a[(j - 2 + N) % N]

for i in range(N - 1):
    print(arr_a[i],end = ' ')
print(arr_a[N - 1])