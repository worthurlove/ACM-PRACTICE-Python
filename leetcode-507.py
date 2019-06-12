
'''
leetcode系列：题号-507
Description:We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

            Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Author:worthurlove
Date:2019.6.12
'''
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sum = 1
        divisors = set([1])
        
        i = 2
        while i*i <= num:
            if num % i == 0:
                divisors.add(i)
                divisors.add(num/i)
                sum = sum + i + num/i
            i += 1
        if sum == num and sum != 1:
            return True
        else:
            return False
            