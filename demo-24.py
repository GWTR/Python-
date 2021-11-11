'''
要求：从键盘录入两个数字，比较两个数字的大小
'''

a=input('请输入第一个整数a')
a=int(a)
b=input('请输入第二个整数b')
b=int(b)

# 比较大小
'''
if a>=b:
    print('a>=b')
else:
    print('a<b')
'''

print('使用条件表达式进入比较')
print(('a>=b') if a>=b else ('a<b'))
