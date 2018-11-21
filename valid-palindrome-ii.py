"""
680. 验证回文字符串 Ⅱ
随机一题
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。


既然要求最多只删除1个字符，那就设定count计数。如果在判断回文的循环过程中，发生不相等，则count++。
最后判断count是否小于2即可。首先初始化指针i=0，j=s.length()-1。


第一个循环i小于j，判断s[i]与s[j]，如果不相等，则j不动，i先往后走一个，即i++（j往前走在下一个循环中），
并且count++。如果相等，则i++，j–。循环结束，如果count小于2，则返回true。
(判断ccbbc这种字符串)

进行第二个循环，循环之前，指针i=0，j=s.length()-1，count=0恢复原值。进入循环i小于j，判断s[i]与s[j]，
如果不相等，则i不动，j往前走一个，即j–，并且count++。如果相等，则i++，j–。循环结束，如果count小于2，则返回true。
(判断cbbcc这种字符串)

"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<2:
            return True
        count=0
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                i+=1
                count+=1
            else:
                i+=1
                j-=1
        if count<2:
            return True
        count=0
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                j-=1
                count+=1
            else:
                i+=1
                j-=1
        if count<2:
            return True  
        return False
