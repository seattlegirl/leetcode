#coding=utf-8
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

先对两个字符串的元素计数，统计两个字符串中每个相同元素的个数相差几个，超过一个为false
"""
import collections
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False  #这种情况直接False “a” “ab”
        ans=0
        counts1=collections.Counter(s)
        counts2=collections.Counter(t)
        for i in counts1:
            if i in counts2:
                ans=ans+abs(counts1[i]-counts2[i])
            else:
                return False  #这种情况直接False “a” “b”或者 "aa" "bb"
        if ans>1:
            return False
        else:
            return True
if __name__ == "__main__":
    print Solution().isAnagram("a", "ab")
    
