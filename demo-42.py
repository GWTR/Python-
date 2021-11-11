"""
字典
python内置的数据结构之一，与列表一样式一个可变数列
以键值对的方式存储数据，字典是一个无序的序列
[]列表
{}字典
python中的字典是根据key查找value所在的位置
hash(key)

字典的创建
最常用的方式：使用花括号
   scores={}
使用内置函数dict()
   dict()
"""

scores = {'张三': 100, '李四': 90, '王五': 80}
print(scores)
print(type(scores))

student = dict(name='Jack', age=20)
print(student)

# 空字典
a = {}
