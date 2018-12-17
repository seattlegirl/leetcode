#coding=utf-8
"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"

首先，我们要知道Excel里这个对应关系是什么样的。从A-Z对应1-26，当列标题进一位变成AA时，列对应的数字变成27。
所以这个题本质上是一个10进制转26进制的问题，不过A对应的是1而不是0，要注意。
"""
"""
- 字符转ASCII码 ord(str)，如ord(‘A’)为65 
- ASCII码转字符 chr(int)，如chr(65)为’A’
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result, dvd = "", n
        while dvd:
            result=chr((dvd-1)%26+ord('A'))+result #注意，不能写成result+=，否则，28会认为是BA
            dvd=(dvd-1)/26
        return result


if __name__ == "__main__":
    for i in xrange(1, 29):
        print Solution().convertToTitle(i)