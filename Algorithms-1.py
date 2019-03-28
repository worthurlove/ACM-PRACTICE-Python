'''
Description:You're given strings J representing the types of stones that are
            jewels, and S representing the stones you have. Each
            character in S is a type of stone you have. You want to know
            how many of the stones you have are also jewels.
            The letters in J are guaranteed distinct, and all characters
            in J and S are letters. Letters are case sensitive, so "a" is
            considered a different type of stone from "A".
            即在数组S中寻找存在于数组J中元素的个数。
Author:worthurlove
Date:2019.3.28
'''


J = input('输入J：')

S = input('输入S：')

def jewelsNum(J,S):
    num = 0

    for i in S:
        if i in J:
            num += 1
    
    return num

print(jewelsNum(J,S))

#一行代码解决问题

# print(sum([1 if i in J else 0 for i in S]))
