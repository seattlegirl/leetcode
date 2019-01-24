#coding=utf-8
"""
205.同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。


同构：要一一对应，顺序也不能变！！！！！！！

将两个字符串分别存到字典中的key和value中，
如果x在key中，但是x对应的value不在另一串中，则错误。
如果x不在key中，但是另一串中的值在value中，则错误。
"""
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic={}
        for i,x in enumerate(s):
            if x in dic.keys() and dic[x]!=t[i]:
                return  False
            elif x not in dic.keys() and t[i] in dic.values():
                return False
            else:
                dic[x]=t[i]
                
        return True

if __name__ == "__main__":
    print Solution().isIsomorphic("egg", "add")
    
        