"""
函数的参数定义
函数定义默认值参数
函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
"""


def fun(a, b=10):
    print(a, b)


# 函数的调用
fun(100)
fun(20, 30)


print('hello', end='\t')
print('world')
