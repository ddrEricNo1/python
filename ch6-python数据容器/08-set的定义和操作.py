"""
集合不支持数据重复，自带去重功能
"""

a = {"传智教育", "黑马程序员"}
b = set()
print(a)
print(b)

# 集合是无序的，所以不支持下标索引访问
# 添加新元素
a.add("python")
print(a)
a.add("传智教育")
print(a)

