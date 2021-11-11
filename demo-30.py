"""
流程控制语句continue
continue语句
用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用
"""

# 要求输出1到50之间所有5的倍数
# 和5的余数为0的数都是5的倍数

for item in range(1,51):
    if item%5==0:
        print(item)


print('=============使用continue语句==============')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)