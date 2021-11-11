"""
字典的常用操作
字典中元素的获取 1. []   2.get()方法
[]取值与使用get()取值的区别
  []如果字典中不存在指定的key，抛出keyError异常
  get()方法取值，如果字典中不存在指定的key，并不会抛出keyError而是返回None
     可以通过参数设置默认的value，以便指定的key不存在时返回
"""

scores = {'张三': 100, '李四': 90, '王五': 80}
print(scores['张三'])
# print(scores['456'])

print(scores.get('张三'))
print(scores.get('456'))
print(scores.get('789', 99))
# 99是在查找789所对的value不存在时，提供的一个默认值
