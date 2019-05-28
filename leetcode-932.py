'''
leetcode系列：题号-932
Description:For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
            For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
            Given N, return any beautiful array A.  (It is guaranteed that one exists.)
Author:worthurlove
Date:2019.5.28
'''
'''
解题思路：
将N个数分成奇数和偶数两个部分
如果奇数部分和偶数部分都是beautArray，那么和起来依然是一个beautifulArray
因为奇数加偶数是一个奇数不可能是另一个数的两倍（即偶数）

还满足两个性质：
即对BeautifulAarry中的每一个元素进行形同的加减乘除某一个数的时候依然保持beautifulArray的条件

删除其中的某一个元素时，剩下的元素依然保持beautifulArray条件

故可以利用分治法的思想进行求解

'''
def beautifulArray(N):
        res = [1]
        while len(res) < N:
                res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        print([i for i in res if i <= N])

beautifulArray(6)