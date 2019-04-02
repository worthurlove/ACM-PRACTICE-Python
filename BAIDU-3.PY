'''
百度笔试题-3：提利昂的赏赐
Description:提利昂收服山地部落之后决定犒赏士卒，本着陈力就列的原则，他决定给五种人以赏赐：
            1.作战能力＞80，并且至少有一项特殊能力的人，每人8000银鹿
            2.作战能力＞85，并且声望＞80的人，每人4000银鹿
            3.作战能力＞90，每人2000银鹿
            4.作战能力＞85的灼人部成员每人1000银鹿
            5.声望＞80的军官每人850银鹿。
            提利昂想要尽量多的犒赏部下，所以只要满足条件即可得到奖赏，即每人可以获得多项赏赐。请你帮他算算自己需要准备多少银鹿，并且他想要知道得到赏赐最多的人是谁，以及它得到的银鹿数量。
Author:worthurlove
Date:2019.4.2
'''
N = int(input())

solider = [0]*6

def change(a):
    if str(a).isdigit():
        a = int(a)
    return a

max_solider = [0]*2
num = 0
for i in range(N):
    max = 0
    solider[:6] = map(change,input().split())
    if solider[1] > 80 and solider[5] > 0:
        max += 8000
    if solider[1] > 85 and solider[2] > 80:
        max += 4000
    if solider[1] > 90:
        max += 2000
    if solider[1] > 85 and solider[4] == 'Y':
        max += 1000
    if solider[1] > 80 and solider[3] == 'Y':
        max += 850

    num += max

    if max > max_solider[1]:
        max_solider[1] = max
        max_solider[0] = solider[0]

print(max_solider[0])
print(max_solider[1])
print(num)