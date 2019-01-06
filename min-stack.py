#coding=utf-8
"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

init()初始化的时候多定义了一个最小值self.min,在每次push和pop操作的时候就判断是否为最小值，保证self.min是最小的。
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack ==None:
            return False
        else:
            self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.stack==None:
            return False
        else:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack==None:
            return False
        else:
            return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

