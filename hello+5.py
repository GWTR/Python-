num = 10
print("你猜一下这个数是什么？")
answer = int(input())

result = answer<num
print("小了一点哦")
print(result)

result = answer>num
print("大了！")
print(result)

result = answer==num
print("就是这个数字")
print(result)

#错误的例子