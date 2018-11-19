"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
 

示例2:

输入: 3
输出: False

双指针法！！！
"""

from math import sqrt
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left=0
        right=int(sqrt(c))
        while left<=right:
            result=left*left+right*right
            if result ==c:
                return True
            else:
                if result>c:
                    right-=1
                else:
                    left+=1
        return False
        