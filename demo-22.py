'''
多分支结构，多选一执行
从键盘录入一个整数 成绩
判断成绩的范围
90-100 A
80-89 B
70-79 C
60-69 D
0-59 E
小于0或者大于100为非法数字（不是成绩的有效范围）
'''

score=int(input('请输入你的成绩：'))
# 开始判断
if score>=90 and score<=100:
    print('A')
elif score>=80 and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
elif score>=0 and score<=59:
    print('E')
else:
    print('非法数字')