"""
列表生成式
列表生成式  生成列表的公式
语法格式： [i*i for i range(1,10)]
注意事项： “表达列表元素的表达式”中通常包含自定义变量
"""

lst = [i for i in range(1, 10)]
print(lst)

# 列表中的元素值为2，4，6，8，10
lst2 = [2 * i for i in range(1, 6)]
print(lst2)

lst3 = [i for i in range(2, 11, 2)]
print(lst3)
