"""
列表元素的查询操作
获取列表元素的多个元素
语法格式：列表名【start：stop：step】
"""

lst=[10,20,30,40,50,60,70,80,90]
# start=1,stop=6,step=1
# print(lst[1:6:1])
print('原列表',id(lst))
lst2=lst[1:6:1]
print('切的片段',id(lst2))

print(lst[1:6]) # 默认步长为1
print(lst[1:6:])
print(lst[:6])
print(lst[1:6:2])

print(lst[::])
print(lst[1::1])

print('=============步长为负数的情况===============')
print(lst)
print(lst[::-1])
print(lst[7::-1])
print(lst[6::-2])
print(lst[6:0:-2])