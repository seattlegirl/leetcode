#coding=utf-8
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

不使用字符串来判断，也就是不使用额外的空间。
可以将原整数翻转，看反转后的整数是否和原来整数相等。
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #负数时，一定不是回文,结尾为0时，不是回文
        if x<0 or (x!=0 and x%10==0):
            return False
        reverse=0
        while x>reverse:
            reverse=reverse*10+x%10
            x=x//10
        return x==reverse or reverse//10==x

if __name__ == "__main__":
    print Solution().isPalindrome(11)


