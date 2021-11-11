#布尔运算符

print("--------------and-并且--------------")

a,b=1,2
print(a==1 and b==2)
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b!=2)

print("--------------or-或者---------------")

print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b==2)
print(a!=1 or b!=2)

print("-------------not-非----------------")

f=True
f2=False
print(not f)
print(not f2)

print("----------in&not in--------------")
s='hello world'
print('w'in s)
print('w'not in s)
print('k'in s)
print('k'not in s)