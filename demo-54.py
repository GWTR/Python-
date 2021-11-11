"""
字符串的查询操作的方法
1. index() 查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError
2. rindex() 查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError
3. find() 查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出-1
4. rfind() 查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出-1
"""

s = 'hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

"""
字符串的大小写转换操作的方法
1. upper() 把字符串所有字符都转成大写字母
2. lower() 把字符串所有字符都转成小写字母
3. swapcase() 把字符串所有大写字母转成小写字母，把所有小写字母转成大写字母
4. capitalize() 把第一个字符转换为大写，其余字符转换成小写
5. title() 把每个单词的第一个字符转换成大写，把每个单词的生于字符转换成小写
"""

m = 'hello,python'
a = m.upper()  # 转成大写之后，会产生一个新的字符串
print(a)
b = a.lower()
print(b)

c = 'heLLo,PytHon'
d = c.swapcase()
print(d)

e = d.capitalize()
print(e)
e = d.title()
print(e)

print('==============字符串内容对齐操作的方法===============')
'''
1. center() 居中对齐，第一个参数指定宽度，第2个参数指定填充符，第2个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
2. ljust() 左对齐，第一个参数指定宽度，第2个参数指定填充符，第2个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
3. rjust() 右对齐，第一个参数指定宽度，第2个参数指定填充符，第2个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
4. zfill() 右对齐，左边用0填充，该方法只接受一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身
'''
s = 'hello,python'
print(s.center(20, '*'))
print(s.ljust(20, '+'))
print(s.rjust(20, '+'))
print(s.zfill(20))
