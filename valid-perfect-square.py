#coding=utf-8
"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False

使用二分查找
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l=1
        r=num
        while l<=r:
            mid=(l+r)//2
            t=mid*mid
            if t<num:
                l=mid+1
            elif t==num:
                return True
            else:
                r=mid-1
        return False

if __name__ == "__main__":
    print Solution().isPerfectSquare(16)
    
    