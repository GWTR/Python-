'''
嵌套循环
循环结构中又嵌套了另外的完整的循环结构，其中内层循环作为外层循环的循环体执行
'''

for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t')
    print()

print('===================打印直角三角形=================')
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='')
    print()

print('===================打印九九乘法表=================')
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j, end='\t')
    print()