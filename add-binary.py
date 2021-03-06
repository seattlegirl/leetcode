#coding=utf-8
"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

int()函数用于将一个字符串或数字转换为整型。语法： 
class int(x, base) 
x–字符串或数字 
base–进制数，默认十进制。 
bin()函数返回一个整型int或者长整数long int的二进制表示。 
bin()运算返回的是二进制。所以前两位是二进制的标志，需要[2:]去除。
>>>bin(10)
'0b1010'
>>> bin(20)
'0b10100'
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=int('0b'+a,2)
        b=int('0b'+b,2)
        return(bin(a+b))[2:]
if __name__ == "__main__":
    print Solution().addBinary("11","1")
