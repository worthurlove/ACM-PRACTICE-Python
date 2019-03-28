'''
Description:Given two integers n and k, return all possible combinations
            of k numbers out of 1 ... n.
Author:worthurlove
Date:2019.3.28
'''

def Combinations(L, k):
 #递归调用解决问题
    n = len(L)
    result = [] 
    for i in range(n-k+1):
        if k > 1:
            newL = L[i+1:]
            Comb= Combinations(newL, k - 1)
            for item in Comb:
                item.insert(0, L[i])
                result.append(item)
        else:
            result.append([L[i]])
    return result



n,k = map(int,input().split())

L = [i for i in range(n)]

print(Combinations(L, k))
