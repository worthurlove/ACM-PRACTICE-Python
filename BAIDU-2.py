
'''
百度笔试题-2：士兵队列
Description:一队士兵在操场上排成一列，士兵总数为n，士兵按照队伍从前往后的顺序从1到n依次编号。每个士兵有各自的身高，第i个士兵的身高为ai。
            兵列队完毕后，将军走到队列的最前面。因为身高不一，有些士兵可能被前面身高更高的挡住了，这样将军就看不到他们。
            将军能看到某个士兵当且仅当他的身高严格大于他前面的所有士兵。
            问将军一共能看到多少个士兵。
Author:worthurlove
Date:2019.4.2
'''
T = int(input())

num = [1]*T
for i in range(T):
    N = int(input())
    height = [0]*N
    height[:N] = map(int,input().split())
    #记录已遍历序列的最大身高
    max = height[0]
    for j in range(1,N):
        if height[j] > max:
            num[i] += 1
            max = height[j]

for i in range(T):
    print(num[i])