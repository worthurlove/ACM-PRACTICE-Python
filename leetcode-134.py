'''
leetcode系列：题号-134
Description:There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
            You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
            You begin the journey with an empty tank at one of the gas stations.
            Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
            Note:
            1.If there exists a solution, it is guaranteed to be unique.
            2.Both input arrays are non-empty and have the same length.
            3.Each element in the input arrays is a non-negative integer.

            Input: 
            gas  = [1,2,3,4,5]
            cost = [3,4,5,1,2]
Author:worthurlove
Date:2019.3.16
'''

'''
解题思路：首先判断所有加油站的油加一起能不能走完全程，如果不够则返回-1，否则接下来的过程
        循环从每个加油站出发：
            判断每个加油站的油加上剩下的油能不能走完去下一个加油站的路
'''
#解法一（超时错误）
class solution:
    def canCompleteCircuit(self,gas,cost)->int:
        #首先判断所有的油够不够跑完全程
        gasCollect = sum(gas)
        gasCost = sum(cost)

        gasNumber = len(gas)

        if gasCost > gasCollect:
            return -1
        
        else:
            for i in range(gasNumber):
                gasCollect = gas[i]
                for j in range(i ,gasNumber + i ):
                    t = j % gasNumber
                    if gasCollect >= cost[t]:
                        gasCollect = gasCollect - cost[t] + gas[(t + 1) % gasNumber]
                    else:
                        break
                if i == (t + 1) % gasNumber:
                    return i + 1
            return -1
#解法2（虽然效率还是很低，但是能通过）
class solution2:
    def canCompleteCircuit(self,gas,cost)->int:
        #首先判断所有的油够不够跑完全程
        gasCollect = sum(gas)
        gasCost = sum(cost)

        if gasCost > gasCollect:
            return -1
        
        else:
            gasNumber = len(gas)

            '''
            与解法一的区别，首先先将cost数组减去gas数组得到一个剩余数组，如果left[i]小于零，则不能从该点出发，从而省去了很多操作
            每次加上下一个left元素即可得到剩余多少油
            '''
            left = [gas[i] - cost[i] for i in range(gasNumber)]

            for i in range(gasNumber):
                if left[i] >= 0:
                    gasCollect = left[i]

                    j = 0#当数组长度为1是，j会出现未定义错误

                    for j in (i+1,gasNumber + i):
                        gasCollect += left[j % gasNumber]
                        if gasCollect < 0:#油不够行驶时则直接退出该点的循环，下一个点重新出发
                            break

                    if (j + 1) % gasNumber == i:
                        return i

                else:
                    continue
            return -1
