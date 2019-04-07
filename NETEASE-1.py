
'''
网易笔试题-1：操作序列
Description小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
1、将a_i放入b序列的末尾
2、逆置b序列
小易需要你计算输出操作n次之后的b序列。
Author:worthurlove
Date:2019.4.7
'''
N = int(input())
a = [0]*N
b = [0]*N
a[:] = map(int,input().split())

for i in range(N):
    if (N-i)%2 == 0:
        b[-int((N -i)/2)] = a[i]
    else:
        b[int((N-i)/2)] = a[i]
        
for j in b:
    print(j,end=' ')