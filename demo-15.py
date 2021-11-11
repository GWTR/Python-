#赋值运算符
abd=3+4
print(abd)
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))

print("-----------支持参数赋值----------")
a=20
a+=30
print(a)
a-=10
print(a)
a*=2
print(a)
print(type(a))
a/=3
print(a)
print(type(a))
a//=2
print(a)
print(type(a))

print("==============支持解包赋值==============")
x,y,z=1,2,3
print(x,y,z)

print("==============交换两个变量的值==============")
a,b=10,20
print("交换之前：")
print(a,b)
a,b=b,a
print("交换之后：")
print(a,b)