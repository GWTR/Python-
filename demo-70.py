"""
斐波那契数列
"""


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 第3位上的数字
print(fib(3))

# 前几位的数字
print('__________________________')
for i in range(1, 7):
    print(fib(i))
