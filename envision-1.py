
'''
远景笔试题-1
Description:输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
Author:worthurlove
Date:2019.4.2
'''
array = [1,2,3,4,5,6,7]
tmp = 0
end = len(array)
i = 0
while i < end:
    if array[i] % 2:
        array.insert(tmp,array.pop(i))
        tmp += 1
        i += 1
    else:
        i += 1
print(array)