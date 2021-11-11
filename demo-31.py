'''
else语句
if条件表达式不成立的时候执行else
没有碰到break的时候执行else
'''
'''
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='888':
        print('密码正确！')
        break
    else:
        print('密码错误！')
else:
    print('账户锁定！')
'''

a=0
while a<3:
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    a+=1
else:
    print('三次密码均错误，账户锁定')
