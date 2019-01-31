#coding=utf-8
"""
696. 计数二进制子串
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
注意：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。

想求得0和1的个数相等的子串，数一下，连续的0,1的个数有多少，构成一个数组找出相邻的两个个数的最小值就好了。
比如“0001111”, 结果是min(3, 4) = 3, 即，("01", "0011", "000111")。

"""

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        num=[] 
        count=1
        for i in range(1,n):
            if s[i]==s[i-1]:
                count+=1
            else:
                num.append(count)
                count=1
        num.append(count) #当最后一次循环时，if中的count无法append到num中，所以在此处append
        return sum(min(x,y) for x,y in zip(num[:-1],num[1:]))
        # l = ['a', 'b', 'c', 'd', 'e','f']
        # print zip(l[:-1],l[1:])
        # [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]

if __name__ == "__main__":
    print Solution().countBinarySubstrings("00110011")
    
        
            