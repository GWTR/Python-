"""
集合的数学操作
"""

s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

# 交集操作
print(s1.intersection(s2))
print(s1 & s2)

# 并集操作
print(s1.union(s2))
print(s1 | s2)

# 差集操作
print(s1.difference(s2))
print(s1-s2)

# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)