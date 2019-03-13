'''
leetcode系列：题号-20
Description:Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

            An input string is valid if:

            1.Open brackets must be closed by the same type of brackets.
            2.Open brackets must be closed in the correct order.
            Note that an empty string is also considered valid.
Author:worthurlove
Date:2019.3.13
'''
class Solution:
    def isValid(self, s: str) -> bool:
        
        stackBracket = []#定义一个栈来匹配这些括号
        for i in s:
            if i == '(' or i == '{' or i == '[':#括号的前一半则入栈
                stackBracket.append(i)
            else:
                if len(stackBracket) == 0:#后一半时，如果栈为空，则也是错误的
                    return False
                else:
                    symbol = stackBracket.pop()#出栈符号，不匹配则非法
                    if (i == ')' and symbol != '(') or (i == '}' and symbol != '{') or (i == ']' and symbol != '['):
                        return False
        
        if len(stackBracket) == 0:#最终栈为空时才合法
            return True
        else:
            return False