"""
什么是元组
元组
   python内置的数据结构之一，是一个不可变序列
不可变序列与可变序列
  不可变序列：字符串、元组
  没有增、删、改的操作
  可变序列：列表、字典
  可以对序列执行增、删、改操作，对象地址不发生改变
"""

'''
元组的创建方式
1. 直接使用小括号
   t=('python','hello',90)
2. 使用内置函数tuple()
   t=tuple(('python','hello',90))
3. 只包含一个元组的元素需要使用逗号和小括号
   t=(10,)
'''

t = ('python', 'hello', 90)
print(t)
print(type(t))

t1 = tuple(('python', 'hello', 90))
print(t1)
print(type(t1))

t3 = ('python')
print(t3)
print(type(t3))

t4 = ('python',)
print(t4)
print(type(t4))

# 空元组
t5 = ()
t5 = tuple()
