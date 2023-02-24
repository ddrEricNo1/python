"""
字符串三种定义方式
    1.单引号定义
    2.双引号定义
    3.三引号定义
"""

a = 'test'
print(a)

b = "test2"
print(b)

c = """test3"""
print(c)

"""
字符串拼接，通过+即可，只能实现字符串与字符串之间的拼接
"""
name = "黑马程序员"
message = "学IT就来 %s" % name
print(message)

class_num = 57
avg_salary = 16781
message = "python大数据学科，北京%s期，毕业平均工资%s" %(class_num, avg_salary)
print(message)
