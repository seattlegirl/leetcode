#coding=utf-8
"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.

求0也就是求其中2*5的个数，也就是5的个数，因为每一个偶数都含2，只要有5肯定有2。
正确的做法是使用n除以5
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=0
        while n>=5:
            n=n//5
            r+=n
        return r
if __name__ == "__main__":
    print Solution().trailingZeroes(5)

