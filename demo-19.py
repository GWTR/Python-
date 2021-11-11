"""
程序的组织结构
1.顺序结构 2.选择结构 3，循环结构
选择结构为 if 语句
循环结构为 while 语句  for in 语句
"""

# 顺序结构
# 程序从上到下顺序地执行代码，中间没有任何的判断和跳转，直到程序结束

'''
把大象装进冰箱一共需要几步
'''
print('-------程序开始-------')
print('1.把冰箱门打开')
print('2.把大象放进冰箱')
print('3.把冰箱门关上')
print('-------程序结束-------')

'''
python一切皆对象，所有对象都有一个布尔值
以下对象的布尔值为False
False
数值（）
None
空字符串
空列表
空元组
空字典
空集合
'''

# 测试对象的布尔值

print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(list()))
print(bool(()))
print(bool(tuple()))
print(bool({}))
print(bool(dict()))
print(bool(set()))
print("===============以上对象的布尔值均为Fslse==============")
