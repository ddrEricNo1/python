my_str = "itheima and itcast"

new_str = my_str.replace("it", "程序")
print(new_str)

"""
字符串的分割
按照指定的分隔符分割字符串，将字符串划分为多个字符串，并存入列表对象中
字符串本身不变，而是得到了一个列表对象
"""

str = "hello python itheima itcast"
result = str.split(" ")
print(result)
print(type(result))
print(str)

# strip去除前后空格
new_str = str.strip()
print(new_str)
# strip(字符串)

str1 = "12 hello"
# 去除前后指定的字符串
new_str1 = str1.strip("12")
print(new_str1)