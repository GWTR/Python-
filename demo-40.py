"""
列表的排序操作
常见的两种方式
1. 调用sort()方法，列表中所有元素默认按照从小到大的顺序进行排序
   可以指定reverse=True，进行降序排序
2. 调用内置函数sorted(),可以指定reverse=True，进行降序排序，原列表不发生改变
"""

lst = [10, 20, 40, 60, 50, 30, 70, 90, 80]
print('排序前的列表\n', lst, id(lst))
lst.sort()
print('排序后的列表\n', lst, id(lst))

# 通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)
print(lst)

lst.sort(reverse=False)
print(lst)

print('==============使用内置函数sorted()对列表进行排序，将产生一个新的列表对象================')
lst2 = [1, 5, 3, 6, 4, 2, 8, 9, 7]
print('排序之前的列表\n', lst2)
lst3 = sorted(lst2)
print('排序之后的列表\n', lst3)

# 通过指定关键字参数，将列表中的元素进行降序排序
lst4 = sorted(lst2, reverse=True)
print(lst4)
