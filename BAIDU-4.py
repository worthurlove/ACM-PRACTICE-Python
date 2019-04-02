s1 = input()

s2 = input()

N = int(input())

num = [0]*N
for k in range(N):

    a,b = map(int,input().split())

    #在给定的上界和实际上界中选择一个较小的，防止越界
    up_limit = min(b,len(s1))

    for i in range(a-1,up_limit - len(s2) + 1):
        t = i
        for j in range(len(s2)):
            if s1[t] != s2[j]:
                j = -1
                break
            else:
                print('j:{}'.format(j))
                t += 1

        if j == len(s2) - 1:
            num[k] += 1
            i += len(s2) - 1
    


for k in range(N):
    print(num[k])