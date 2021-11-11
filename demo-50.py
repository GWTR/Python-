"""
集合元素的判断操作
1. 集合元素的判断操作
   in或者not in
2. 集合元素的新增操作
   调用add()方法，一次添中一个元素
   调用update()方法，至少添中一个元素
3. 集合元素的删除操作
   调用remove()方法，一次删除一个指定元素，如果指定的元素不存在抛出keyerror
   调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不抛出异常
   调用pop()方法，一次只删除一个任意元素
   调用clear()方法，清空集合
"""

s = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(10 in s)
print(20 not in s)
print(100 not in s)

print('========集合元素的新增操作=======')
s.add(100)
print(s)

s.update({1, 2, 3})
print(s)
s.update([101,102,103])
print(s)
s.update((500,600))
print(s)

print('========集合元素的删除操作=======')
s.remove(100)
print(s)
# s.remove(700)
# print(s)
s.discard(500)
print(s)
s.pop()
print(s)
s.clear()
print(s)