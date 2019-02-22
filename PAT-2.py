'''
PAT中文系列：1010
Describe:设计函数求一元多项式的导数，以指数递降方式输入多项式非零项系数
和指数（绝对值均不超过1000的整数）。数字间以空格分隔。
Author:worthurlove
Date:2018.12.13
'''

input_arr = [int(i) for i in input().split()]


#指数合法性检测
for i in range(1,len(input_arr),2):
    if input_arr[i] > 1000:
        print("请输入合法数值")
        break

for i in range(0,len(input_arr) - 1,2):

    #“零多项式”的指数和系数都是 0，但是表示为 0 0。
    if len(input_arr) == 2 and input_arr[1] == 0:
        input_arr[0] = 0

    elif input_arr[i + 1] == 0:#如果指数为0，则在求导之后消失，在数组中删除
       #需要先删除最后一个指数，否则会越界出现错误
        del input_arr[i + 1]
        del input_arr[i]
    else:
        input_arr[i] = input_arr[i] * input_arr[i + 1]
        input_arr[i + 1] -= 1
    
for i in range(len(input_arr) - 1):
    print(input_arr[i],end = ' ')
print(input_arr[-1])
