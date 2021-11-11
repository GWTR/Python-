"""
列表元素的增加操作
1. append() 在列表的末尾添加一个元素
2. extend() 在列表的末尾至少添加一个元素
3. insert() 在列表的任意位置添加一个元素
4. 切片 在列表的任意位置添加至少一个元素
"""

lst=[10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))

lst2=['hello','python']
lst.extend(lst2)
# 在列表的末尾一次性添加多个元素
print(lst)

# 在任意位置添加一个元素
lst.insert(1,90)
print(lst)

# 在任意位置添加至少一个元素
lst3=[True,False,'hello']
lst[1:]=lst3
print(lst)