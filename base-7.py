#coding=utf-8
"""
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。

采用除基取余法 
1234/7,商176,余2 
176/7,商25,余1 
25/7,商3,余4 
3/7,商0,余3 
从上到下依次是个位、十位、百位、千位 
所以,最终结果为(3412)7.
"""
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        new_num=abs(num)
        result=""
        while new_num:
            result=str(new_num%7)+result
            new_num//=7
        if num<0:
            result="-"+result
        return result 

if __name__ == "__main__":
    print Solution().convertToBase7(1234)

