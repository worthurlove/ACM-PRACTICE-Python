'''
leetcode系列：题号-43
Description:大数相乘
Author:worthurlove
Date:2019.4.22
'''
def multiply(num1: str, num2: str):
    result = []
    num1_a = []
    num2_a = []
    for i in num1:
        num1_a.append(int(i))
        
    for j in num2:
        num2_a.append(int(j))
        
        
    result = [0]*len(num2_a)
    
    for i in range(len(num1_a) - 1,-1,-1):
        #被乘数中的每一位与乘数相乘

        tmp = []#存放一位数与乘数相乘之后的结果

        f = 0#用于判断每一个数相乘是否有进位
        for j in range(len(num2_a) - 1,-1,-1):
            tmp.insert(0,(num1_a[i] * num2_a[j] + f)% 10 )
            f = int((num1_a[i] * num2_a[j] + f) / 10)
        if f > 0:
            tmp.insert(0,f)
            
        f = 0
        for k in range(len(tmp) - 1,-1,-1):
            t = len(result) - 1 - (len(num1_a) - 1 - i) - (len(tmp) - 1 - k)
            if t < 0:
                m = tmp[k] + f
                result.insert(0,m % 10)
                f = int(m/10)
                if f > 0 and k == 0:
                    result.insert(0,f)
            else:
                add_r = result[t] + tmp[k] + f
                result[t] = add_r % 10
                f = int(add_r / 10 )
                if f > 0 and k == 0:
                    result.insert(0,f)
    s = ''
    for i in range(len(result) - 1):
        if result[i] != 0:
            for j in range(i,len(result)):
                s = s + str(result[j])
            break
    if len(s) == 0:
      s = s + str(result[-1])
    print(s)



num1 = '79362'

num2 = '217'

multiply(num1,num2)