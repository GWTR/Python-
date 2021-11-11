"""
字符串的切片操作
字符串是不可变类型
不具备增、删、改等操作
切片操作将产生新的对象
"""

s = 'hello,python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
newstr = s1 + s3 + s2
print(s1)
print(s2)
print(newstr)

print('-------------切片[start:end:step]--------------')
print(s[1:5:1])  # 从1开始截到5（不包含5），步长为1
print(s[::2])  # 　默认从０卡死hi，没有写结束，默认到字符串的最后一个元素，步长为２
print(s[::-1])
print(s[-6::1])
