#coding=utf-8
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true


1.拿到一个题首先要考虑有几种情况： 
1)空和奇数个直接排除 
2)剩下偶数个，若第一个就是右括号直接排除，不是右括号再入栈。 
2.画个流程图辅助。 
3.for else的用法。for循环完后执行else语句块，若for中有break，则跳过else。 
4.l[-1]为l的最后一个元素。

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """      
        
        if len(s)%2==1 :  #奇数个直接排除 （题目中说空字符串也算有效字符串）
            return False
        d={'{':'}','[':']','(':')'}
        stack=[]
        for i in s: #第一个就是右括号的直接删除
            if i in d:
                stack.append(i)
            
            else:
                if not stack or d[stack.pop()]!=i: #注意if中的前后顺序，顺序错则意思和结果错
                    return False

        return stack==[]

if __name__ == "__main__":
    print Solution().isValid("()[]{}")
    print Solution().isValid("()[{]}")
            
                
        