"""
字符串的编码转换
编码解码的方式
编码： 将字符串转换为二进制数据
解码： 将bytes类型的数据转换成字符串类型
"""

s='天涯共此时'
# 编码
print(s.encode(encoding='GBK'))  # 在GBK这种编码格式中，一个中文占用两个字符
print(s.encode(encoding='UTF-8'))  # 在UTF-8这种编码格式中，一个中文占用三个字符

# 解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
