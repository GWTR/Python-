"""
集合生成式
用于生成集合的公式
  {i*i for i in range(1,10)}
"""

s = {i for i in range(10)}
print(s)
s = {i*i for i in range(10)}
print(s)