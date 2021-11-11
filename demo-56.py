"""
判断字符串的方法
1. isidentifier() 判断字符串是不是合法的标识符
2. isspace() 判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）
3. isalpha() 判断指定的字符串是否全部由字母组成
4. isdecimal() 判断指定字符串是否由十进制的数字组成
5. isnumeric() 判断指定字符串是否全部由数字组成
6. isalnum() 判断指定字符串是否全部由字母和数字组成
"""

s = 'hello,python'
print('1', s.isidentifier())
print('2', 'hello'.isidentifier())
print('3', '张三_'.isidentifier())
print('4', '张三_123'.isidentifier())

print('5', '\t'.isspace())

print('6', 'abc'.isalpha())
print('7', '张三'.isalpha())
print('8', '张三1'.isalpha())

print('9', '123'.isdecimal())
print('10', '一二三'.isdecimal())
print('11', 'Ⅱ'.isdecimal())

print('12', '123'.isnumeric())
print('13', '一二三'.isnumeric())
print('14', 'Ⅱ'.isnumeric())

print('15', '加油123'.isalnum())
