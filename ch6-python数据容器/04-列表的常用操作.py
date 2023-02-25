mylist = ["itcast", "itheima", "python"]
print(mylist.index("itheima"))

# 列表中追加元素
# .append

# 删除指定位置元素
# del mylist[2]
obj = mylist.pop()
print(mylist)
print(obj)

# remove从前到后删除第一个满足条件的元素
data = [1, 2, 3, 4, 1]
data.remove(1)
print(data)