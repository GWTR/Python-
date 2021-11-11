name='张三'
age=20
print(type(name),type(age))

print('我叫'+name+'今年，'+str(age)+'岁')


print('---------------str()将其他类型转化成str类型--------------')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)))

print('---------------int()将其他类型转化成int类型--------------')
s1='128'
f1=98.7
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))     #将str转成int类型，字符串为数字串
print(int(f1),type(int(f1)))     #将float转成int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2)))    #将str转成int类型，报错，因为字符串为小数串

print('---------------float()将其他类型转化成float类型--------------')
a1='128.98'
a2='76'
a3=True
a4='hello'
a5=98
print(type(a1),type(a2),type(a3),type(a4),type(a5))
print(float(a1),float(a2),float(a3),float(a5))
print(type(float(a1)))