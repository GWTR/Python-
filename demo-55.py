"""
字符串劈分操作的方法
split()
1. 从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
2. 以通过参数sep指定劈分字符串的劈分符
3. 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独做为一部分
rsplit()
1. 从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
2. 以通过参数sep指定劈分字符串的劈分符
3. 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独做为一部分
"""

s = 'hello world Python'
lst = s.split()
print(lst)
s1 = 'hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

s = 'hello world Python'
lst = s.rsplit()
print(lst)
s1 = 'hello|world|Python'
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))
