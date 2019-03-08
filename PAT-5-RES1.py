'''
PAT数据结构题目系列：排序(升序)
Description:本题旨在测试各种不同的排序算法在各种数据情况下的表现。各组测试数据特点如下：
            数据1：只有1个元素；
            数据2：11个不相同的整数，测试基本正确性；
            数据3：103个随机整数；
            数据4：104个随机整数；
            数据5：105个随机整数；
            数据6：105个顺序整数；
            数据7：105个逆序整数；
            数据8：105个基本有序的整数；
            数据9：105个随机正整数，每个数字不超过1000。
Author:worthurlove
Date:2019.3.6
'''
#算法一：冒泡排序
#算法二：选择排序
#算法三：快速排序
#算法四：归并排序
#算法五：堆排

import numpy as np

N = int(input())

sort_Arr = [0]*N

sort_Arr[:N] = map(int,input().split())

# sort_Arr = np.random.randint(-2147483648,2147483647,size = N)#随机产生N个小于1000的整数

# print(sort_Arr)
#冒泡排序
def bubble_Sort(Arr):
    for i in range(1,N):#总共进行N - 1次循环冒泡，从1开始
        for j in range(0,N - i):#每次循环比上一轮少一次冒泡
            if Arr[j] > Arr[j + 1]:
                flag = Arr[j + 1]#作为交换的中间变量
                Arr[j + 1] = Arr[j]
                Arr[j] = flag
    print(Arr)


#选择排序
def select_Sort(Arr):
    for i in range(N - 1):#最后留下来的那个数就是最大的数，不需要再比较选择
        for j in range(i + 1,N):
            if Arr[i] > Arr[j]:#和比自己小的元素交换位置
                min = Arr[j]
                Arr[j] = Arr[i]
                Arr[i] = min
    print(Arr)

#快速排序
'''
核心思想是分治，在待排序的数组中，任选一个元素pivot作为基准将待排序元素划分为独立的两个部分L[1,...,k - 1]和L[k,...,n]使得
L[1,...,k - 1]中的所有元素小于pivot,L[K,...,n]中的所有元素大于或等于pivot,则pivot放在了其最终位置L[k]上，这个过程称为一趟快速排序。
'''
def quick_Sort(Arr,low,high):
    if low < high:
        pivot = partion(Arr,low,high)
        quick_Sort(Arr,low,pivot - 1)
        quick_Sort(Arr,pivot + 1,high)#PIVOT + 1基准元素不再放入划分中，否则进入死循环


def partion(Arr,low,high):
    pivot = Arr[low]
    while low < high:#非常巧妙的方法
        while low < high and Arr[high] >= pivot:#当左端元素大于或等于pivot时则high减1，直到遇到比其小的元素时结束
            high -= 1

        Arr[low] = Arr[high]#将遇到的那个比基准（也就是第一个数）小的元素赋值给Arr[low],这样就覆盖了这个元素，但是pivot存储了这个基准值，所以它被保存了下来
                            #而A[high]的值并没有改变，等待着比pivot大的第一个元素或者pivot覆盖

        while low < high and Arr[low] < pivot:
            low += 1

        Arr[high] = Arr[low]#与上述同理，两个方向进行

    Arr[low] = pivot#此时，low == high

    return low

    
# bubble_Sort(sort_Arr)
# select_Sort(sort_Arr)
quick_Sort(sort_Arr,0,N - 1)
for i in range(N):
    if i != (N - 1):
        print(sort_Arr[i],end = ' ')
    else:
        print(sort_Arr[i])
