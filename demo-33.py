"""
二重循环中的break和continue
二重循环中的break和continue用于控制本层循环
"""

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()

"""
知识点总结
1.range()函数
  生成整数数列；起始值默认为0；步长默认为0
2.循环结构
  while 用于次数不固定的循环；起始条件不成立一次都不执行
  for-in用于遍历可迭代对象
3.break&continue&else
  break退出当前循环结构
  continue结束当前循环进入下一次循环
  else: if……else  while……else   for……else
4.嵌套循环
  外层循环执行一次内层循环执行完整一次
  while和for-in互相嵌套
"""