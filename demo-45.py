"""
获取字典视图的三个方法
keys()  获取字典中所有key
values()  获取字典中所有value
items()  获取字典中所有key，value对
"""

scores = {'张三': 100, '李四': 90, '王五': 80}
# 获取所有的key
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有的key组成的视图转成列表

# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))

# 获取所有的key-value对
items=scores.items()
print(items)
print(list(items))  # 转换之后的列表元素是由元组组成的