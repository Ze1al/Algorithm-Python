# 两个栈实现一个队列

class Solution:
    def __init__(self):
        self.stack1 = []   # 作为一个入栈
        self.stack2 = []   # 作为一个出栈

    def push(self, a):
        self.stack1.append(a)

    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                a = self.stack1.pop()
                self.stack2.append(a)
            return self.stack2.pop()