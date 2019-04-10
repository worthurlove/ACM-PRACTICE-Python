N = 'abc3(A)asd2(asd1(er))'

N = input()

#定义一个栈

stack_bracket = []

stack_num = []

rep = [0]*100

i = 0
j = 0#重复的字符串

while i < len(N):

    if str(N[i]).isdigit():
        stack_num.append(int(N[i]))
        stack_bracket.append(str(N[i + 1]))
        i += 2
        while str(N[i]).isalpha():
            stack_bracket.append(str(N[i]))
            i += 1


    elif str(N[i]) == ')':
            s = []
            i += 1
            while stack_bracket[-1] != '(':
                s.insert(0,stack_bracket.pop())
             
            stack_bracket.pop()

            for k in range(int(stack_num.pop())):
                stack_bracket.extend(s)
    elif str(N[i]) == ']':
            s = []
            i += 1
            while stack_bracket[-1] != '[':
                s.insert(0,stack_bracket.pop())
             
            stack_bracket.pop()

            for k in range(int(stack_num.pop())):
                stack_bracket.extend(s)
    elif str(N[i]) == '}':
            s = []
            i += 1
            while stack_bracket[-1] != '{':
                s.insert(0,stack_bracket.pop())
             
            stack_bracket.pop()

            for k in range(int(stack_num.pop())):
                stack_bracket.extend(s)
    else:
        stack_bracket.append(str(N[i]))
        i += 1


s = ''
for i in stack_bracket:
    s = i + s
print(s)

                



