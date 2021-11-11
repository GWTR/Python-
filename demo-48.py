"""
为什么将元组设计成不可变序列
1. 在多任务环境下，同时操作对象时不需要加锁
2. 因此在程序中尽量使用不可变序列
注意事项  元组中存储的是对象的引用
a 如果元组中对象本身不可变对象，则不能再引用其他对象
b 如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变
"""

t = (10, [20, 30], 40)
print(t)
print(type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))

# 尝试将t[1]修改为100
print(id(100))
# t[1]=100
# 元组不允许修改元素
# 由于[20,30]为列表，而列表是可变序列，所以可以向列表中添加元素，列表的内存地址不变
t[1].append(100)
print(t)
print(id(t[1]))

"""
元组的遍历
元组是课迭代对象，所以可以使用for…in进行遍历
t=tuple(('hello','world',98))
for item in t:
    print(item)
"""

t = ('hello', 'python', 98)
# 使用索引
print(t[0])
print(t[1])
print(t[2])
# 使用for in
for item in t:
    print(item)
