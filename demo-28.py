'''
for-in循环
in表达从（字符串、序列等）中依次取值，又称遍历
for-in遍历的对象必须是可迭代对象
for-in的语法结构
for 自定义的变量 in 可迭代的对象
    循环体
循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
'''

for item in 'Python':
    print(item)

# range() 产生一个整数序列，-->也是一个可迭代对象
for i in range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可以将自定义变量写为”_“
for _ in range(5):
    print('人生苦短，我用Python')

print('===========使用for循环计算1到100的偶数和============')
sum=0
for a in range(1,101):
    if a%2==0:
        sum+=a
print('和为',sum)

print('+++++++++++输出100到999之间的水仙花数+++++++++++++')
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    if ge**3+shi**3+bai**3==item:
        print(item)
