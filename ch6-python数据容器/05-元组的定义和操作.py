"""
列表元素可以修改，但元组不可以修改
元组一旦定义完成，不可以修改
"""

t1 = (1, 'Hello', True)
t2 = tuple()

# 单个元素的元组需要在后面加上逗号表示该容器为元组
t3 = (2,)

print(t1)
print(t2)
print(type(t3))

t5 = ((1, 2), (3,))
print(t5)

"""
index()
count()
len()
"""