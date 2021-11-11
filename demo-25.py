# range()的三种创建方式
'''
1. 只有一个参数（小括号中只给了一个数）
2. 给了两个参数（小括号中给了两个数）
3. 给了三个参数（小括号中给了三个数）
'''
r=range(10)  # 默认从0开始，默认步长为1
print(list(r))  # 用于查看range对象中的整数数列  -->list是列表的意思

r=range(1,10)
print(list(r))

r=range(1,10,2)
print(list(r))

# 判断指定的整数 在序列中是否存在 in，not in
print(10 in r)
print(9 in r)
print(10 not in r)