"""
格式化字符串
"""

name = '张三'
age = 20
print('我叫%s,今年%d岁' % (name, age))

print('我的名字是{0}，年龄为{1}'.format(name, age))

print(f'我叫{name},今年{age}岁了')


print('%10d'% 99)  # 表示的是宽度
print('hellohello')

print('%f' % 3.1415926)
print('%.3f' % 3.1415926)
print('%10.3f' % 3.1415926)


print('++++++++++++++++++++++++++++++++')

print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))   # 表示一共三位数
print('{0:.4}'.format(3.1415926))
print('{0:.3f}'.format(3.1415926))
print('{0:10.3f}'.format(3.1415926))