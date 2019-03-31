'''
百度面试题-1：编码转换
Description:小B最近对电子表格产生了浓厚的兴趣，她觉得电子表格很神奇，功能远比她想象的强大。她正在研究的是单元格的坐标编号，她发现表格单元一般是按列编号的，第1列编号为A，第2列为B，以此类推，第26列为Z。之后是两位字符编号的，第27列编号为AA，第28列为AB，第52列编号为AZ。之后则是三位、四位、五位……字母编号的，规则类似。
            表格单元所在的行则是按数值从1开始编号的，表格单元名称则是其列编号和行编号的组合，如单元格BB22代表的单元格为54列中第22行的单元格。
            小B感兴趣的是，编号系统有时也可以采用RxCy的规则，其中x和y为数值，表示单元格位于第x行的有第y列。上述例子中的单元格采用这种编码体系时的名称为R22C54。
            小B希望快速实现两种表示之间的转换，请你帮忙设计程序将一种方式表示的坐标转换为另一种方式。
Author:worthurlove
Date:2019.4.1
'''
N = int(input())
#写两个函数，分别解决转换问题

#excel格式到RxCy格式
def excel_to_rxcy(S):
    num1 = 0
    num2 = 0
    for i in S:
        if str(i).isalpha():
            num1 = num1*26 + ord(i) - 64
        else:
            num2 = num2*10 + ord(i) - 48
    print('R'+str(num2)+'C'+str(num1))

#RxRy格式到Excel格式
def rxry_to_excel(S):
    #求出C的列表位置
    C_index = S.index('C')
    sub1 = S[1:C_index]
    sub2 = S[C_index + 1:]
    
    num1 = 0
    num2 = 0

    for i in sub1:
        num1 = num1*10 + ord(i) - 48
    for i in sub2:
        num2 = num2*10 + ord(i) - 48

    SR = ''
    while num2 != 0:
        tmp = num2%26
        '''
        此处有坑，和10进制不同，没有0，所以整除时需要特殊考虑
        '''
        if tmp == 0:
            tmp = 26
            SR = chr(tmp + 64) + SR
            num2 = int(num2/26) - 1
        else:
            SR = chr(tmp + 64) + SR
            num2 = int(num2/26)

    print(SR+str(num1))



for i in range(N):
    S = input()
    #首先判断输入的是excel格式还是rxry格式
    if S[0] == 'R' and str(S[1]).isdigit() and 'C' in S:
        rxry_to_excel(S)

    else:
        excel_to_rxcy(S)
    