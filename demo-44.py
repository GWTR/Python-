"""
字典的常用操作
1. key的判断
   in 指定的key在字典中存在返回True
   not in 指定的key在字典中不存在返回False
2. 字典元素的删除
   del scores['zhangsan']
3. 字典元素的新增
  scores['zhangsan']=90
"""

scores = {'张三': 100, '李四': 90, '王五': 80}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']
# print(scores)
# scores.clear()
print(scores)

scores['陈六']=98
print(scores)
scores['陈六']=100
print(scores)
