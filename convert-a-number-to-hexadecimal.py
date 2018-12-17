#coding=utf-8
"""
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

1610/16=100……10(A)； 

100 /16=  6……4； 

6  /16=  0……6；  

1610(10)=64A(16)


负数转换成八进制、十六进制，只需在补码(二进制)的基础上，3位合成一位计算，或者4位合成一位计算

十进制如何转换成二进制
我们如何把十进制的-3，转换成二进制表示呢？首先我们将 -3 的绝对值 +3 转换成二进制，假设是为int类型(32位)的，那么二进制表示为：

0000 0000 0000 0000 0000 0000 0000 0011
负数转换成二进制分为3步：

1、 首先将负数转换为对应的原码

-3 的原码为(也就是+3转换成二进制后的字符串)：

0000 0000 0000 0000 0000 0000 0000 0011
2、 再将原码的每一位做取反操作得到反码。

取反操作：0变为1 、 1变为0；取反后的结果即为：

1111 1111 1111 1111 1111 1111 1111 1100
3、 将反码+1得到补码

1111 1111 1111 1111 1111 1111 1111 1101
"""
"""
在处理ASCII码时,需要用到的两个函数方法. 
Ⅰ.chr()方法:将十进制数转化为基础字符

chr(65) 
‘A’
Ⅱ.ord():将字符转化为十进制数

ord(‘A’) 
65
"""
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "0"

        result = []
        while num and len(result) != 8:  #不懂？？？？？and len(result) != 8
            """
            a=60 b=13
            a = 0011 1100  b = 0000 1101
            &	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,
            否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
            """
            h = num & 15
            if h < 10:
                result.append(str(chr(ord('0') + h)))
            else:
                result.append(str(chr(ord('a') + h-10)))
            """
            >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，
            >> 右边的数字指定了移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111
            """
            num >>= 4
        result.reverse()
        # return result

        return "".join(result)

if __name__ == "__main__":
    print Solution().toHex(26)
    
            
