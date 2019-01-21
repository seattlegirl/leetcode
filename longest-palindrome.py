#coding=utf-8
"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

主要考虑字母在字符串中出现的次数是奇数次还是偶数次
"""
import collections
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        k=0
        counts=collections.Counter(s)
        for i in counts:
            if counts[i]%2==0:
                result+=counts[i]
            else:
                result+=counts[i]-1#当某个字母的个数是单数时，去掉一个组成回文串
                k=1 #且这时，一定能保证有一个放在回文中间的字母
        return result+k

if __name__ == "__main__":
    print Solution().longestPalindrome("abccccdd")
    

