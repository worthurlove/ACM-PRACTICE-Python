'''
Description:给定一个01组成的数组，找出连续1最多的子串
Author:worthurlove
Date:2019.4.13

'''
S = input()

s_input = []

for i in S:
    s_input.append(i)

i = len(s_input) - 1

s_copy = s_input.copy()
while i >= 0:
    if s_copy[i] == '1':
        s_input.pop()
        s_input.insert(0,s_copy.pop())
        i -= 1
    else:
        break

nums = []


num = 0
for i in s_input:
    if i == '1':
        num += 1
    else:
        nums.append(num)
        num = 0
nums.append(num)

print(max(nums))


