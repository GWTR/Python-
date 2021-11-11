"""
字符串操作的其他方法
replace()
第一个参数指定被替换的子串，第2个参数指定替换子串的字符串，该方法返回替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数
join()
将列表或元组中的字符串合并成一个字符串
"""

s = 'hello,python'
print(s.replace('python', 'java'))

s = 'hello,python,python,python'
print(s.replace('python', 'java', 2))

lst = ['hello', 'java', 'python', 'C++']
print('|'.join(lst))
print(''.join(lst))

print('+'.join('python'))