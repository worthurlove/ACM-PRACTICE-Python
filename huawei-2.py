'''
leetcode系列：题号-394
Description:Given an encoded string, return it's decoded string.

        The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

        You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

        Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

        华为笔试题改编要求逆序输出，但是不考虑多位数的情况
Author:worthurlove
Date:2019.4.11
'''


s = 'abc10(A)'


#定义一个栈

stack_bracket = []

stack_num = []

i = 0

while i < len(s):
    
    if str(s[i]).isdigit():
        nums = int(s[i])
        #考虑多位数的情况
        while str(s[i + 1]).isdigit():
            nums = nums*10 + int(s[i + 1])
            i += 1
        stack_num.append(nums)
        stack_bracket.append(str(s[i + 1]))
        i += 2
        while str(s[i]).isalpha():
            stack_bracket.append(str(s[i]))
            i += 1


    elif str(s[i]) == ')':
            part = []
            i += 1
            while stack_bracket[-1] != '(':
                part.insert(0,stack_bracket.pop())
             
            stack_bracket.pop()

            for k in range(int(stack_num.pop())):
                stack_bracket.extend(part)
    elif str(s[i]) == ']':
            part = []
            i += 1
            while stack_bracket[-1] != '[':
                part.insert(0,stack_bracket.pop())
             
            stack_bracket.pop()

            for k in range(int(stack_num.pop())):
                stack_bracket.extend(part)
    elif str(s[i]) == '}':
            part = []
            i += 1
            while stack_bracket[-1] != '{':
                part.insert(0,stack_bracket.pop())
             
            stack_bracket.pop()

            for k in range(int(stack_num.pop())):
                stack_bracket.extend(part)
    else:
        stack_bracket.append(str(s[i]))
        i += 1


part = ''
for i in stack_bracket:
    part = i + part
print(part)

                



