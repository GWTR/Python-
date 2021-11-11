"""
流程控制语句break
break语句
用于结束循环结构，通常与分支结构if一起使用
"""

'''
从键盘录入密码，最多录用三次
如果正确就结束循环
'''
"""
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '888':
        print('密码正确')
        break
    else:
        print('密码错误，请您再次输入密码')
print('输入三次错误，账户锁定')
"""
a=0
while a<3:
    pwd = input('请输入密码：')
    if pwd == '888':
        print('密码正确')
        break
    else:
        print('密码错误，请您再次输入密码')
    a+=1



