'''
leetcode系列：题号-122
Description:Say you have an array for which the ith element is the price of a given stock on day i.
            Design an algorithm to find the maximum profit.
            You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
            Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
Date:2019.3.115
'''
#贪心算法解决该问题
'''
解题思路：假想一个股票波动的折线图，将折线非下降的部分相加即为最大的利益
'''
class Solution:
    def maxProfit(self,prices) -> int:

        profit = 0

        #需要考虑输入数组为空的情况
        if prices:
            start = end = prices[0]
        else:
            return 0

        #寻找每一个上升部分的起点与终点
        for price in prices:

            '''
            当曲线从高峰开始下降的时候，第一次下降记录前一个高低峰之差，之后的下降同步start与end的值，不买也不出，直到曲线反弹
            '''
            if price < end:
                profit += (end - start)
                start = end = price


            else:
                end = price

        #曲线的最后一个上升阶段需要在循环外加上
        profit += (end - start)

        return profit
