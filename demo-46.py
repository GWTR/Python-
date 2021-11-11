"""
字典元素额遍历
for item in scores:
    print(item)
"""

scores = {'张三': 100, '李四': 90, '王五': 80}
# 字典元素的遍历
for item in scores:
    print(item)

'''
字典的特点
字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
字典中的元素都是无序的
字典中的key必须是不可变对象
字典也可以根据需要动态地伸缩
字典会浪费较大的内存，是一种使用空间换时间的数据结构
'''

"""
字典生成式
内置函数zip()
  用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
{item.upper():price for item,price in zip(items,prices)}
"""

items = ['Fruits', 'Books', 'Others']
prices = [96, 87, 86, 45]
d = {item: price for item, price in zip(items, prices)}
print(d)

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
