"""
集合
python语言提供的内置数据结构
与列表、字典一样都属于可变类型的序列
集合是没有value的字典

集合的创建方式
1. 直接使用{}
   s={'python','hello',98}
2. 使用内置函数set()
   s=set(range(6))
   print(s)
   print(set([3,4,53,56]))
   print(set((3,4,43,435)))
   print(set('python'))
   print(set({124,3,4,5}))
   print(set())
"""

# 1. 直接使用{}
s = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6}  # 不允许重复
print(s)

# 2. 使用内置函数set()
s1 = set(range(6))
print(s1, type(s1))
s2 = set([1, 2, 3, 5, 8, 9])
print(s2, type(s2))

s3=set('python')
print(s3)

# 定义一个空集合
s4={}
print(s4,type(s4))
s5=set()
print(s5,type(s5))