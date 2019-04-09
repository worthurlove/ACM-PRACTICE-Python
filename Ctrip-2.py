'''
携程笔试题-2：最小子串
Description:给定一个数字序列，求最小的两个子串和相加的结果
      
Author:worthurlove
Date:2019.4.9
'''
NUM = []

NUM.extend(map(int,input().split()))

#先找出最小和的子序列


res = [0]*len(NUM)

sum_1 = 0
start = 0
end = 0


'''
动态规划找出最小子段
'''
res[0] = NUM[0]
for i in range(1,len(NUM)):

    res[i] = min(res[i - 1] + NUM[i], NUM[i])
print(res)
#记录最小值
sum_1 = min(res)

#找出第一个最小子段结束的位置，如果有同样的最小子段则等着下一次寻找
end = res.index(sum_1)
#找出最小子段的开始位置
for i in range(end,-1,-1):
    if res[i] == NUM[i]:
        start = i
        break

#最小子段是整个串
if start == 0 and end == len(NUM) - 1:
    print(sum_1)

#只剩后半截
elif start == 0:
    sum_2 = min(res[end+1:len(NUM)])
    print('sum_2:{}'.format(sum_2))

    print(sum_1+sum_2)
#只剩前半截
elif end == len(NUM) - 1:
    sum_2 = min(res[0:start])
    print('sum_2:{}'.format(sum_2))
    print(sum_1+sum_2)

else:
    sum_2  = min(res[0:start])

    res_1 = [0]*(len(NUM) - 1 - end)
    res_1[0] = NUM[end + 1]
    for i in range(1,len(NUM) - end):
        res_1[i] = min(res_1[i - 1] + NUM[i], NUM[i])
    sum_3 = min(res_1)

    print('sum_2:{},sum_3:{}'.format(sum_2,sum_3))
    print(sum_1 + min(sum_2,sum_3))

        

    