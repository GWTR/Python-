
# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('hello world')
print("hello world")

# 可以输出含有运算符的表达式
print(3 + 1)

# 将文件输出到文件中.注意点：1.所使用的盘符需要存在。2.使用file=
# a+如果文件不存在就创建，存在就再文件内容后面继续追加
fp = open('E:/text.txt', 'a+')
print('hello world', file=fp)
fp.close()

# 不进行换行输出
print('hello', 'world', 'Python')
