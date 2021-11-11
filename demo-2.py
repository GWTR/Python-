#转义字符
print('hello\nworld')     #\+转义功能的首字母   n-->newline的首字母表示换行
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')     #world将hello进行了覆盖
print('hello\bworld')    #\b是退一个格

print('http:\\\\www.baidu.com')
print('老师说:\'dajiahao\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r/R
#注意事项，最后一个字符不能使\
print(r'hello\nworld')