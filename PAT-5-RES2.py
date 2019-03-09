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

总结：归并排序和堆排序都能AC，快排并不能
'''
#算法四：归并排序
#算法五：堆排


N = int(input())

sort_Arr = [0]*N

sort_Arr[:N] = map(int,input().split())

help_Arr = sort_Arr.copy()#辅助数组，用于归并操作

'''
归并排序：归并也是基于分治的思想，“归并”的含义是将两个或两个以上的有序表组合成一个新的有序表。
时间复杂度：一共进行log2(n)次排序，每次排序的时间复杂度为1,2,4,...,n等比数列，数量级为n，所以时间复杂度为nlog2(n)


快排的关键步骤是partion（划分）：将一个数组划分成左右两个序列

归并排序的关键步骤是merge(归并)：将两个有序数组合并

'''
def merge_Sort(Arr,low,high):#递归调用归并排序
    if low < high:
        mid = int((low + high)/2)#从中间划分两个子序列

        merge_Sort(Arr,low,mid)#对左侧子序列进行递归排序

        merge_Sort(Arr,mid + 1,high)#对右侧子序列进行递归排序

        merge(Arr,low,mid,high)#归并左右子序列

def merge(Arr,low,mid,high):

    #首先将待排序左右两个子序列复制到辅助序列中
    for i in range(low,high + 1):
        help_Arr[i] = sort_Arr[i]
    
    
    i = low#左侧序列从low开始
    j = mid + 1#右侧序列从mid + 1开始
    k = i#用于遍历数组

    while i <= mid and j <= high:#当左右两个子序列都没有遍历完成时循环

        if help_Arr[i] < help_Arr[j]:#由于左右两个序列是两个有序的子序列，所以当左侧序列中的元素比右侧的小时，直接放入排序序列中，比右侧大时，右侧直接放入排序序列
            sort_Arr[k] = help_Arr[i]
            k += 1
            i += 1

        else:
            sort_Arr[k] = help_Arr[j]
            k += 1
            j += 1

    while i <= mid:#当左右两个序列有一个已经遍历完时，则直接遍历另一个序列放入排序序列
        sort_Arr[k] = help_Arr[i]
        k += 1
        i += 1

    while j <= high:
        sort_Arr[k] = help_Arr[j]
        k += 1
        j += 1



'''
堆排序：堆排序是一种树形选择排序方法。(小根堆为例)
'''
#建堆（也就是向上调整操作）
def build_Heap(Arr):
    help_Arr[0] = 0
    help_Arr[1:] = Arr.copy()#辅助数组，从1开始计数

    # print(help_Arr)

    for i in range(2,len(help_Arr)):#从第二个数开始

        help_Arr[0] = help_Arr[i]#用来记录待插入的元素，相当于哨兵

        flag = i#记录当前节点位置

        father_point = int(i/2)#父亲节点位置

        while father_point != 0 and help_Arr[0] < help_Arr[father_point]:#一直是待插入节点在与父亲节点做比较

            help_Arr[flag] = help_Arr[father_point]#当前节点与父亲节点交换，但是父亲节点可以最后再赋值

            flag = father_point

            father_point = int(father_point/2)

        help_Arr[flag] = help_Arr[0]

    return help_Arr


#向下调整堆(根节点输出之后)
def adjust_Down(Arr):
    flag = 1

    min = 1#记录要交换的子节点

    Arr[0] = Arr[1]
    while flag * 2 < len(Arr):
    #找出子节点中的较小者
        left = flag * 2
        if left + 1 < len(Arr):
            right = left + 1
            min = left if Arr[left] < Arr[right] else right
        else:
            min = left
        
        if Arr[0] > Arr[min]:#如果子节点中的较小者比当前节点小，则交换位置
            Arr[flag] = Arr[min]
            flag = min
            Arr[min] = Arr[0]
        else:#否则调整结束
            break
    # print(Arr)
    

#堆排序
def sort_Heap(Arr):
    out_arr = build_Heap(Arr)
    for i in range(N):
        if i < N - 1:
            print(out_arr[1],end = ' ')
            out_arr[1] = out_arr.pop()
        else:
            print(out_arr[1])
        adjust_Down(out_arr)#输出一个元素，调整一次



# merge_Sort(sort_Arr,0,N - 1)

sort_Heap(sort_Arr)


# for i in range(N):
#     if i != (N - 1):
#         print(sort_Arr[i],end = ' ')
#     else:
#         print(sort_Arr[i])




